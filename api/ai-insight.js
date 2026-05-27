export default async function handler(req, res) {
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
        model: "openrouter/free",
        messages: [
          {
            role: "user",
            content: prompt
          }
        ]
      })
    });

    const data = await response.json();

    res.status(200).json({
      insight: data.choices?.[0]?.message?.content || "No AI insight generated."
    });

  } catch (error) {
    res.status(500).json({
      insight: "Error generating AI insight."
    });
  }
}