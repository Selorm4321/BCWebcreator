const functions = require('firebase-functions');
const cors = require('cors')({ origin: true });
const { Resend } = require('resend');

const resend = new Resend('re_57VwY4gk_4J8nSREjejqbAUsdGZTzXXtr');

// Dialogflow Webhook Fulfillment
exports.dialogflowFulfillment = functions.https.onRequest((request, response) => {
    cors(request, response, async () => {
        try {
            console.log('Dialogflow Request body: ', JSON.stringify(request.body));

            const intentName = request.body.queryResult?.intent?.displayName;
            const parameters = request.body.queryResult?.parameters;

            if (intentName === 'Quote - Contact Info') {
                const name = parameters['person']?.name || 'A customer';
                const email = parameters['email'] || 'No email provided';
                const phone = parameters['phone-number'] || 'No phone provided';

                const rawData = JSON.stringify(parameters, null, 2);

                const emailContent = `
                    <h2>New Quote Request from Dialogflow Chatbot!</h2>
                    <p><strong>Name:</strong> ${name}</p>
                    <p><strong>Email:</strong> ${email}</p>
                    <p><strong>Phone:</strong> ${phone}</p>
                    <hr/>
                    <h3>Raw Data Captured:</h3>
                    <pre>${rawData}</pre>
                `;

                // Send email
                await resend.emails.send({
                    from: 'BC Web Creator Bot <onboarding@resend.dev>',
                    to: ['bcwebcreator@gmail.com'],
                    subject: `New Lead: ${name} wants a quote!`,
                    html: emailContent
                });

                console.log('Email sent successfully!');
            }

            response.status(200).send({
                fulfillmentText: "I've passed your info along to the BC Web Creator team!"
            });

        } catch (error) {
            console.error('Webhook error:', error);
            response.status(500).send('Error');
        }
    });
});
