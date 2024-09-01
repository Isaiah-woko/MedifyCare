fetch("/pay/config")
  .then((result) => {
    return result.text().then(text => {
      console.log("Config response:", text); // Log the raw response
      return JSON.parse(text); // Attempt to parse as JSON
    }).catch((error) => {
      console.error("Error parsing /pay/config response:", error);
      throw error;
    });
  })
  .then((data) => {
    // Initialize Stripe.js
    const stripe = Stripe(data.publicKey);
    // checkout 
    document.querySelector("#submitBtn").addEventListener("click", () => {
      // Get Checkout Session ID
      fetch("/pay/create-checkout-session")
        .then((result) => {
          return result.text().then(text => {
            console.log("Session response:", text); // Log the raw response
            return JSON.parse(text); // Attempt to parse as JSON
          }).catch((error) => {
            console.error("Error parsing /pay/create-checkout-session response:", error);
            throw error;
          });
        })
        .then((data) => {
          console.log(data);
          // Redirect to Stripe Checkout
          return stripe.redirectToCheckout({sessionId: data.sessionId});
        })
        .then((res) => {
          console.log(res);
        });
    });
  })
  .catch((error) => {
    console.error("Error in payment.js:", error);
  });
