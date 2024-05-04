from openai import OpenAI

# Set up OpenAI API key
key = 'api key'

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=key,
)

# Example post
post = """
"Hello room hunters!
Seeking a roommate to share a lovely 3 Bed/3.5 Bath townhouse, newly constructed about 8 years ago. Currently the room is still occupied, but tenant is ok with showing the room now, and officially available 2/1/24. Complex is extremely peaceful and quiet. A good night's sleep is a perk not to be taken for granted :)

Your Room:
* Rent: $1400 (1yr lease)
* SPACIOUS master bed room with 240 sq ft total (14'2"" x 13' for room + 7'6""x7'4"" for walk-in closet)
* Huge walk-in closet (55 sq ft) that has a door-mounted full-sized mirror
* Very nice and sunny/bright with nice breeze
* LUXURIOUS private bathroom with 2 sinks, standing shower, and tub (never been used)
* New/lovely granite sink countertop with endless amount of cabinets in the private bathroom
* 1/3 of utility bill will be added separately based on usage (internet, electricity, water), which is usually ~$130-150/person pending tenant usage
* 1-year lease
* Payment due when signing: 1st month's rent as deposit + $33 background check

About You:
* Friendly! And hopefully share some of the interests listed below with us :)
* Working professional, good credit, drama free, reliable, pays rent/utility on time and cleans up common area after using
* Light cooking (once or twice a week)
* No smoking, drugs or pets please
About your 2 roommates:
* Male 20s & 30s
* One self employed, the other in construction management
* Both love being sociable, watching Netflix in living room, hockey, guitar, one-wheeling, boxing, tennis!

Residence Features:
* Spacious 3 bed/3.5 bath townhouse with 1700 sq ft
* Modern open floor plan with high ceilings and is completely and beautifully furnished
* New hardwood floors and carpet
* Huge balcony on 2nd floor
* In-home washer and dryer
* Basic cable and super fast high-speed internet ready (170+Mbps consistently throughout the day)
* Fully equipped kitchen with beautiful granite countertops and new appliances
* Fully furnished living room
* Mini Ping Pong table and weights set in the living room
* Lots of parking outside the townhouse unit within few steps of walking distance
* Lots of storage units throughout the Townhouse

Neighborhood:
* Quiet, beautiful and safe neighborhood (Berryessa Rd. and Jackson St.)
* Close to major freeways: 680, 101, and 880
* 2-min drive to Safeway (24 hrs), CVS (24 hrs), Costco, Ranch 99, Starbucks, King Eggroll, and many close-by plazas with variety of restaurants and grocery stores. 7-Leaves, Gong Cha and ShareTea are extremely close by if you are into good milk tea.
* 8-min drive to Great Mall, 15min to Valley Fair, and 10min to downtown San Jose
* Close to PayPal and eBay campuses
Please contact if you're interested or have any questions."
"""

def extract_accomodation_details(text):
    prompt = get_details() + text

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    content = response.choices[0].message.content.strip()

    return content

def get_details():
    return '''Please retrieve the following details from the following facebook post.
    1. Rent
    2. Location or Address is the address of the available room. retrieve full address. If no location found, return empty string
    3. From Date is from when the room is available. If date format is 'Jan 2024' then convert it into '01/01/2024'. If the room is available now then return 4/27/2024.
    4. To Date is untill when the room is available. If date format is 'Jan 2024' then convert it into '01/01/2024'. If there is lease duration then calculate the date and append to output.
    5. bed
    6. bath
    7. amenities
    If you can't find the information from the article then return ''. 
    Return response in json format. The format of the json should be this,
    {
        "rent": "1200",
        "location": "San Jose, CA",
        "fromDate": "07/01/2024",
        "toDate": "08/01/2024",
        "bedrooms": "2",
        "bathrooms": "3",
        "amenities": ["swimming pool", "gym", "parking"]
    }

    Post:
    ==================================

    '''

# if __name__ == '__main__':
#     extract_accomodation_details()

