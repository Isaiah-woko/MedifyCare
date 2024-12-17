
from flask import render_template, request, flash
from flask_login import login_required, current_user
from flask import Blueprint
from flask_socketio import emit, join_room
from webapp import socketio
from ..auth.models import User, Role
from .chat_controller import save_message, get_messages
from .. import db
from .models import Message

chat_blueprint = Blueprint(
    'chat',
    __name__,
    template_folder='../templates/chat',
    url_prefix="/chat"
)


@chat_blueprint.route('/doctors', methods=['GET', 'POST'])
@login_required
def my_doctor():
    doctors = db.session.query(
        User.id,
        User.username,
        User.specialty,
        User.bio,
        # User.is_available  # Assuming Ahed have a field for availability
    ).join(User.roles).filter(Role.name == 'doctor').all()
    check = 0
    specialties = list(set(doctor.specialty for doctor in doctors))
    if request.method == 'POST':
        phone_number = request.form.get('videoCallID')
        doctor_id = request.form.get('doctorId')
        msg = Message.query.filter_by(sender_id=current_user.id, receiver_id=doctor_id).first()
        # if the user already send a message update just the number
        if msg:
            msg.phone_number = phone_number
        else:
            msg = Message(sender_id=current_user.id, receiver_id=doctor_id, phone_number=phone_number)
        db.session.add(msg)
        db.session.commit()
        check = 1
    if check:
        check = 0
    return render_template('patient_home.html', doctors=doctors, specialties=specialties)


@chat_blueprint.route('/consult/<username>', methods=['GET'])
@login_required
def consult_doc(username):
    # Fetch doctor details based on username
    doctor = User.query.filter_by(username=username).first_or_404()

    # fetch old messages
    messages = get_messages(current_user.id, doctor.id)

    # Render the chat page with the doctor's details
    return render_template('consult_doc.html', doctor=doctor, messages=messages)


@chat_blueprint.route('/patients', methods=['GET'])
@login_required
def my_patients():
    # Fetch the list of patients who have sent messages to the doctor
    messages = Message.query.join(User, Message.sender_id == User.id)\
        .filter(Message.receiver_id == current_user.id)\
        .join(Role, User.roles)\
        .filter(Role.name == 'patient')\
        .distinct().all()

    # For each patient, fetch the first message they sent
    patient_data = []
    for patient in patients:
        first_message = Message.query.filter_by(sender_id=patient.id, receiver_id=current_user.id)\
                                     .order_by(Message.timestamp.asc()).first()

        patient_data.append({
            'patient': patient,
            'first_message': first_message
        })

    return render_template('doc_home.html', patient_data=patient_data)


@chat_blueprint.route('/patient/<username>', methods=['GET'])
@login_required
def view_patient_messages(username):
    # Ensure the current user is a doctor
    # if not current_user.is_doctor:
    #     return redirect(url_for('home'))

    # Fetch the patient
    patient = User.query.filter_by(username=username).first_or_404()

    # Fetch the messages between the doctor and the patient
    messages = Message.query.filter(
        ((Message.sender_id == patient.id) & (Message.receiver_id == current_user.id)) |
        ((Message.sender_id == current_user.id) & (Message.receiver_id == patient.id))
    ).order_by(Message.timestamp.asc()).all()

    return render_template('doctor_chat.html', patient=patient, messages=messages)


@socketio.on('connect')
def handle_connect():
    print(f"{current_user.username} connected.")


@socketio.on('disconnect')
def handle_disconnect():
    print(f"{current_user.username} disconnected.")


@socketio.on('join_room')
def handle_join_room(room):
    join_room(room)
    print(f"User joined room: {room}")


@socketio.on('send_message')
@login_required
def handle_send_message(data):
    room = data['room']
    doctor_username, patient_username = room.split('_')

    # Determine the receiver based on who is sending the message
    if current_user.username == doctor_username:
        # If the current user is the doctor, the receiver is the patient
        receiver = User.query.filter_by(username=patient_username).first()
    else:
        # Otherwise, the current user is the patient, and the receiver is the doctor
        receiver = User.query.filter_by(username=doctor_username).first()

    if receiver:
        # Save the message using the save_message function
        message = save_message(receiver_id=receiver.id, content=data['message'])

        print(f"Emitting message to room {room}: {message.content}")

        # Emit the message to the room with additional details
        socketio.emit('receive_message', {
            'message': message.content,
            'sender': current_user.username  # Include sender's username
        }, room=room)
    else:
        # Handle case where the receiver is not found
        emit('error', {'msg': 'Receiver not found'}, room=room)
