# Freight Truck Orders Generator

This project generates realistic freight truck orders in JSON format using the Anthropic Claude API.

## Features
- Generates 20 realistic freight truck orders
- Each order includes:
  - `order_id`: Unique order identifier (e.g., ORD-2025-001)
  - `pickup_location`: Nested object with `city`, `state`, and `zipcode`
  - `delivery_location`: Nested object with `city`, `state`, and `zipcode`
  - `weight_lbs`: Weight in pounds (5000-45000 lbs)
  - `equipment_required`: "Dry Van", "Refrigerated", or "Flatbed"
  - `commodity`: Type of freight (e.g., General Freight, Food Products, etc.)
  - `ready_date`: Date in October 2025 (YYYY-MM-DD)
  - `delivery_deadline`: 2-7 days after ready_date
- Realistic logistics data and routes
- Output saved as `orders.json`

## Output Format Example
```json
{
  "order_id": "ORD-2025-001",
  "pickup_location": {
    "city": "Dallas",
    "state": "TX",
    "zipcode": "75201"
  },
  "delivery_location": {
    "city": "Houston",
    "state": "TX",
    "zipcode": "77002"
  },
  "weight_lbs": 3500,
  "equipment_required": "Dry Van",
  "commodity": "General Freight",
  "ready_date": "2025-10-15",
  "delivery_deadline": "2025-10-17"
}
```

## Usage
1. **Install dependencies**
   - Requires Python 3
   - Install the `anthropic` Python package:
     ```bash
     pip install anthropic
     ```
2. **Set your Anthropic API key**
   - Open `generate ordes.py`
   - Replace the `api_key = " "` line with your actual API key
3. **Run the script**
   ```bash
   python3 'generate ordes.py'
   ```
4. **Check the output**
   - The generated orders will be saved in `orders.json` in the same folder

## File Descriptions
- `generate ordes.py`: Main script to generate orders using Anthropic Claude API. The prompt enforces a nested object structure for locations.
- `orders.json`: Output file containing the generated freight orders in the required format.
- `README.md`: Project documentation and usage instructions.

## Notes
- The script uses the Claude Sonnet model for generation.
- The prompt strictly enforces the nested object format for `pickup_location` and `delivery_location`.
- Make sure your API key is valid and has sufficient quota.
- If the output format is incorrect, check the prompt in the script and ensure it matches the required structure.

## License
This project is for demonstration and educational purposes only.
