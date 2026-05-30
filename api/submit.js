import { Resend } from 'resend';

const resend = new Resend(process.env.RESEND_API_KEY);

export default async function handler(req, res) {
    if (req.method !== 'POST') {
        return res.status(405).json({ error: 'Method Not Allowed' });
    }

    try {
        const { name, phone, email, address, insurance_claim, services, message } = req.body;

        // Validate required fields
        if (!name || !phone || !email || !message) {
            return res.status(400).json({ error: 'Missing required fields: name, phone, email, and message are required.' });
        }

        // Format services list
        const servicesList = Array.isArray(services) && services.length > 0
            ? services.map(s => s.charAt(0).toUpperCase() + s.slice(1)).join(', ')
            : 'Not specified';

        // Format insurance claim
        const insuranceClaim = insurance_claim === 'yes' ? 'Yes' : 'No';

        const htmlBody = `
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin: 0; padding: 0; background-color: #EDF4F7; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
    <table width="100%" cellpadding="0" cellspacing="0" style="background-color: #EDF4F7; padding: 40px 20px;">
        <tr>
            <td align="center">
                <table width="600" cellpadding="0" cellspacing="0" style="background-color: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 20px rgba(26, 45, 58, 0.08);">

                    <!-- Header -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #1A2D3A 0%, #2C4A5A 100%); padding: 36px 40px; text-align: center;">
                            <h1 style="color: #00B4D8; font-size: 24px; margin: 0 0 8px 0; font-weight: 700;">🎉 New Lead Received!</h1>
                            <p style="color: #8AAAB7; font-size: 15px; margin: 0;">Congratulations! Looks like you have a new lead from the Trident website.</p>
                        </td>
                    </tr>

                    <!-- Body -->
                    <tr>
                        <td style="padding: 36px 40px;">

                            <!-- Contact Info -->
                            <h2 style="color: #1A2D3A; font-size: 16px; text-transform: uppercase; letter-spacing: 0.08em; margin: 0 0 20px 0; border-bottom: 2px solid #00B4D8; padding-bottom: 10px;">Contact Details</h2>

                            <table width="100%" cellpadding="0" cellspacing="0" style="margin-bottom: 32px;">
                                <tr>
                                    <td style="padding: 10px 0; border-bottom: 1px solid #EDF4F7; color: #4E7282; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; width: 140px; vertical-align: top;">Name</td>
                                    <td style="padding: 10px 0; border-bottom: 1px solid #EDF4F7; color: #1A2D3A; font-size: 15px; font-weight: 600;">${name}</td>
                                </tr>
                                <tr>
                                    <td style="padding: 10px 0; border-bottom: 1px solid #EDF4F7; color: #4E7282; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; vertical-align: top;">Phone</td>
                                    <td style="padding: 10px 0; border-bottom: 1px solid #EDF4F7; color: #1A2D3A; font-size: 15px;">
                                        <a href="tel:${phone}" style="color: #00B4D8; text-decoration: none;">${phone}</a>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 10px 0; border-bottom: 1px solid #EDF4F7; color: #4E7282; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; vertical-align: top;">Email</td>
                                    <td style="padding: 10px 0; border-bottom: 1px solid #EDF4F7; color: #1A2D3A; font-size: 15px;">
                                        <a href="mailto:${email}" style="color: #00B4D8; text-decoration: none;">${email}</a>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 10px 0; border-bottom: 1px solid #EDF4F7; color: #4E7282; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; vertical-align: top;">Address</td>
                                    <td style="padding: 10px 0; border-bottom: 1px solid #EDF4F7; color: #1A2D3A; font-size: 15px;">${address || 'Not provided'}</td>
                                </tr>
                                <tr>
                                    <td style="padding: 10px 0; border-bottom: 1px solid #EDF4F7; color: #4E7282; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; vertical-align: top;">Services</td>
                                    <td style="padding: 10px 0; border-bottom: 1px solid #EDF4F7; color: #1A2D3A; font-size: 15px;">${servicesList}</td>
                                </tr>
                                <tr>
                                    <td style="padding: 10px 0; color: #4E7282; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; vertical-align: top;">Insurance Claim</td>
                                    <td style="padding: 10px 0; color: #1A2D3A; font-size: 15px;">${insuranceClaim}</td>
                                </tr>
                            </table>

                            <!-- Message -->
                            <h2 style="color: #1A2D3A; font-size: 16px; text-transform: uppercase; letter-spacing: 0.08em; margin: 0 0 16px 0; border-bottom: 2px solid #00B4D8; padding-bottom: 10px;">Message</h2>
                            <div style="background-color: #F7FAFC; border-left: 4px solid #00B4D8; padding: 20px; border-radius: 0 8px 8px 0; color: #1A2D3A; font-size: 15px; line-height: 1.7; margin-bottom: 32px;">
                                ${message.replace(/\n/g, '<br>')}
                            </div>

                            <!-- Quick Action -->
                            <table width="100%" cellpadding="0" cellspacing="0">
                                <tr>
                                    <td align="center">
                                        <a href="tel:${phone}" style="display: inline-block; background-color: #00B4D8; color: #ffffff; text-decoration: none; padding: 14px 36px; border-radius: 8px; font-size: 14px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em;">
                                            📞 Call ${name} Now
                                        </a>
                                    </td>
                                </tr>
                            </table>

                        </td>
                    </tr>

                    <!-- Footer -->
                    <tr>
                        <td style="background-color: #F7FAFC; padding: 24px 40px; text-align: center; border-top: 1px solid #EDF4F7;">
                            <p style="color: #4E7282; font-size: 12px; margin: 0;">This lead was submitted via the Trident Roofing &amp; Exteriors website contact form.</p>
                            <p style="color: #B5CFD8; font-size: 11px; margin: 8px 0 0 0;">© ${new Date().getFullYear()} Trident Roofing &amp; Exteriors</p>
                        </td>
                    </tr>

                </table>
            </td>
        </tr>
    </table>
</body>
</html>
        `.trim();

        const { data, error } = await resend.emails.send({
            from: 'Roofing Website <leads@tridentroofingandexteriors.ca>',
            to: 'info@tridentroofingandexteriors.ca',
            subject: `New Lead: ${name} — Trident Roofing Website`,
            html: htmlBody,
            reply_to: email,
        });

        if (error) {
            console.error('Resend error:', error);
            return res.status(500).json({ error: 'Failed to send email. Please try again.' });
        }

        console.log('Email sent successfully:', data);
        return res.status(200).json({ success: true, message: 'Message sent successfully.' });

    } catch (error) {
        console.error('Server error:', error);
        return res.status(500).json({ error: 'Internal Server Error' });
    }
}
