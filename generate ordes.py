import anthropic
import json

# Set your API key here
api_key = " "

client = anthropic.Anthropic(api_key=api_key)

prompt = """
Generate 20 realistic freight truck orders in JSON array format. Make them look like real logistics data.

Required format for each order:
{
  \"order_id\": \"ORD-2025-001\",
  \"pickup_location\": {
    \"city\": \"Dallas\",
    \"state\": \"TX\",
    \"zipcode\": \"75201\"
  },
  \"delivery_location\": {
    \"city\": \"Houston\",
    \"state\": \"TX\",
    \"zipcode\": \"77002\"
  },
  \"weight_lbs\": 3500,
  \"equipment_required\": \"Dry Van\",
  \"commodity\": \"General Freight\",
  \"ready_date\": \"2025-10-15\",
  \"delivery_deadline\": \"2025-10-17\"
}

Requirements for each order:
- order_id: \"ORD-2025-XXX\" (XXX = 3-digit number starting from 001)
- pickup_location: Use real major US cities with correct state codes and real zipcodes, as an object with city, state, and zipcode fields
- delivery_location: Use different real US cities, create realistic routes (e.g., Chicago to Dallas, LA to Phoenix), as an object with city, state, and zipcode fields
- weight_lbs: Realistic weights between 5000-45000 lbs
- equipment_required: Choose realistically based on commodity - \"Dry Van\", \"Refrigerated\", or \"Flatbed\"
- commodity: Realistic freight types - \"General Freight\", \"Food Products\", \"Electronics\", \"Building Materials\", \"Automotive Parts\", \"Consumer Goods\"
- ready_date: Dates in October 2025 (format: YYYY-MM-DD), spread throughout the month
- delivery_deadline: 2-7 days after ready_date depending on distance

Make it realistic:
- Refrigerated equipment for food products
- Flatbed for building materials
- Heavier loads for building materials, lighter for electronics
- Longer delivery windows for cross-country routes
- Use major freight corridors (TX, CA, IL, GA, FL, NY, PA, OH)

Output ONLY the JSON array, no explanation, no markdown.
"""

try:
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=8000,
        temperature=0.3,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    orders_json = response.content[0].text.strip()
    
    # Remove markdown code blocks if present
    if orders_json.startswith("```"):
        orders_json = orders_json.split("```")[1]
        if orders_json.startswith("json"):
            orders_json = orders_json[4:]
        orders_json = orders_json.strip()
    
    # Validate JSON
    parsed = json.loads(orders_json)
    
    if not isinstance(parsed, list):
        raise ValueError("Response is not a JSON array")
    
    print(f"Generated {len(parsed)} orders")
    
    # Save to file with pretty formatting
    with open("orders.json", "w") as f:
        json.dump(parsed, f, indent=2)
    
    print("✓ orders.json created successfully")
    
except anthropic.APIError as e:
    print(f"API Error: {e}")
except json.JSONDecodeError as e:
    print(f"Invalid JSON received: {e}")
    print("Raw response:", orders_json[:200])
except Exception as e:
    print(f"Error: {e}")