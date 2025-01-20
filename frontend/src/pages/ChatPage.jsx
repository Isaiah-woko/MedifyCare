import { useParams } from 'react-router-dom';
import React, { useState, useRef, useEffect } from 'react';
import ReconnectingWebSocket from 'reconnecting-websocket';
import { MessageList } from 'react-chat-elements';
import { FaPlus } from 'react-icons/fa';
import { LuAArrowDown } from 'react-icons/lu';
import { Scrollbars } from 'react-custom-scrollbars-2';
import '../chatPage.css'

export default function ChatPage() {
    const { id } = useParams();
    const [inputValue, setInputValue] = useState('');
    const [chatHistories, setChatHistories] = useState({});
    const [currentUser, setCurrentUser] = useState(id || 'default');
    const scrollbarRef = useRef();
    const [showPopup, setShowPopup] = useState(false);
    const ws = useRef(null);

    const formatTime = (date) => {
        let hours = date.getHours();
        let minutes = date.getMinutes();
        const ampm = hours >= 12 ? 'PM' : 'AM';
        hours = hours % 12;
        hours = hours || 12;
        minutes = minutes < 10 ? '0' + minutes : minutes;
        return `${hours}:${minutes} ${ampm}`;
    };

    useEffect(() => {
        ws.current = new ReconnectingWebSocket('ws://websocket-url');

        ws.current.onopen = () => {
            console.log('WebSocket connection established');
            ws.current.send(JSON.stringify({ type: 'join', userId: currentUser }));
        };

        ws.current.onmessage = (event) => {
            const message = JSON.parse(event.data);
            if (message.userId === currentUser) {
                setChatHistories((prev) => ({
                    ...prev,
                    [currentUser]: [...(prev[currentUser] || []), message],
                }));
            }
        };

        ws.current.onclose = () => {
            console.log('WebSocket connection closed');
        };

        return () => {
            if (ws.current) ws.current.close();
        };
    }, [currentUser]);

    const handleSendMessage = () => {
        if (inputValue.trim()) {
            const currentTime = new Date();
            const formattedTime = formatTime(currentTime);

            const newMessage = {
                position: 'right',
                type: 'text',
                text: inputValue,
                time: formattedTime,
                userId: currentUser,
            };

            setChatHistories((prev) => ({
                ...prev,
                [currentUser]: [...(prev[currentUser] || []), newMessage],
            }));

            if (ws.current && ws.current.readyState === WebSocket.OPEN) {
                ws.current.send(JSON.stringify(newMessage));
            }

            setInputValue('');
        }
    };

    useEffect(() => {
        if (scrollbarRef.current) {
            scrollbarRef.current.scrollToBottom();
        }
    }, [chatHistories, currentUser]);

    const messages = chatHistories[currentUser] || [];

    return (
<section>
    <div className='h-20'></div>
<main className=''>
            <div className="flex h-[90dvh] bg-[#dea1252e] w-2/4 m-auto rounded-lg shadow-lg">
                <div className="flex flex-1 flex-col">
                    <Scrollbars className="flex-1" ref={scrollbarRef}>
                        <div className="flex-1 overflow-y-auto p-4 max-w-[80%] min-w-[20%]">
                            <MessageList
                                className="message-list "
                                lockable
                                toBottomHeight="100%"
                                dataSource={messages.map((message) => ({
                                    position: message.position,
                                    type: message.type,
                                    text: (
                                        <div className='my-4'>
                                            <p className='p-4'>{message.text}</p>
                                            <p className="flex justify-end text-xs text-gray-400">
                                                {message.time}
                                            </p>
                                        </div>
                                    ),
                                }))}
                            />
                        </div>
                    </Scrollbars>

                    <div className="flex border-t p-2">
                        <input
                            type="text"
                            placeholder="Type a message..."
                            className="mr-2 flex-1 rounded border border-[#eee] bg-[#f1f1f1] p-2"
                            value={inputValue}
                            onChange={(e) => setInputValue(e.target.value)}
                            onKeyDown={(e) => {
                                if (e.key === 'Enter') handleSendMessage();
                            }}
                        />
                        <button
                            onClick={() => setShowPopup(!showPopup)}
                            className="relative mr-2 rounded bg-[#e3e3e3] p-2 text-white"
                        >
                            <FaPlus className="w-6 text-gray-400" />
                        </button>
                        <button
                            className="rounded bg-custom-blue p-2 text-white"
                            onClick={handleSendMessage}
                        >
                            <LuAArrowDown className="w-6 text-gray-400" />
                        </button>
                    </div>
                </div>
            </div>
        </main>
</section>
    );
}
