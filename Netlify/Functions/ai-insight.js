const fetch = require("node-fetch");

exports.handler = async function () {

  const prompt = `
You are a business data analyst.

Analyze this Superstore dashboard summary:
Total Sales: 805,853.84
Average Sales: 91.58
Top Category: Office Supplies
Regions: West, East, Central, South

Write a short business insight and one recommendation.
`;

  try {

    const response = await fetch("https://openrouter.ai/api/v1/chat/completions", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${process.env.OPENROUTER_API_KEY}`,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        model: "openai/gpt-3.5-turbo",
        messages: [
          {
            role: "user",
            content: prompt
          }
        ]
      })
    });

    const data = await response.json();

    return {
      statusCode: 200,
      body: JSON.stringify({
        insight: data.choices[0].message.content
      })
    };

  } catch (error) {

    return {
      statusCode: 500,
      body: JSON.stringify({
        insight: "AI request failed."
      })
    };

  }
};