# CS50 Final Project – 'Happiness is in giving'

"Happiness is in Giving" transcends the boundaries of a typical donation platform. It serves as a transformative force, inspiring individuals to enact meaningful change in the world. Through this project, participants not only contribute to humanitarian aid but also become agents of environmental sustainability and promoters of personal well-being.

By facilitating donations and volunteer efforts, "Happiness is in Giving" empowers people to address pressing global issues while fostering a sense of interconnectedness and compassion. 

Ultimately, "Happiness is in Giving" embodies the belief that true happiness is found in the act of giving back to others and the planet. It's a platform that not only facilitates positive change but also nurtures a collective spirit of generosity, kindness, and hope for a better world.

## Distinctiveness
The website "Happiness is in giving" stands out as a platform that not only makes it effortless for individuals to support communities globally but also fosters a profound impact on various fronts:

### Environmental Impact
- Protecting the Planet: We tackle textile waste head-on, diverting clothing directly to those in need to reduce landfill waste and harmful emissions.

### Humanitarian Aid

- Helping Others: Every donation, big or small, creates a meaningful impact in communities, inspiring others with stories of empowerment.

### Home Organization

- Maintaining Clean Spaces: We simplify decluttering by providing an easy donation process, turning cluttered closets into organized homes.

## Complexity
This project aims to integrate with the Stripe API to facilitate donations or subscriptions for monthly contributions. The complexity lies in implementing a seamless user experience for both one-time donations and recurring subscriptions while ensuring the security and reliability of payment processing through Stripe.

Integrating in-page donation updates using Fetch API and JSON involves making asynchronous calls to the server to update donation information and dynamically switching between view and edit modes for the supported fields without a page reload.

Additionally, the website features an image carousel on the front page aimed at delighting users with captivating visuals, animated via CSS transforms.

-  The `script.js` file contains JavaScript code that adds interactivity and functionality to the web pages of the project. It handles client-side scripting tasks such as DOM manipulation, and event handling.

- 	The `styles.css` file defines the visual styling for a web application. It implements a responsive design, ensuring compatibility with various screen sizes. The layout includes a navigation bar, image carousels, and donation forms styled with buttons and input fields. Additionally, it features flexbox-based container styles for flexible layout arrangements. Media queries are utilized to adjust styling based on the viewport width, optimizing the user experience across different devices.

- 	The `about_us.html` page showcases the impact of the project on people, community, and the planet. It also displays the total amount of money collected through donations and the remaining amount needed to ship packages that families are eagerly awaiting.

- 	The `add_new_listing.html` file contains the HTML markup for the `NewListingForm` form. 

- 	The `cancel.html` page is displayed when the monetary donation process is canceled by the user. It provides a message acknowledging the cancellation and offers the option to return to the home page.

- 	The `categories.html` page displays categories based on age, ranging from 0 to 15 years, with an option for other categories.

- 	The `donation_checkout.html` page offers users the option to make either a one-time donation or a monthly donation. It seamlessly integrates with Stripe for secure payment processing.

- 	The `index.html` page provides non-authenticated users with the option to make either a one-time or monthly donation and features sliding images for visual appeal. Authenticated users can view their own donations.

- 	The `layout.html` file serves as the template layout for the project and includes a navigation bar.

- 	The `listing.html` page displays the picture and details of an individual donation listing. Users have the option to claim a donation if they are not the listing owner, or edit the donation if they are the listing owner.

- 	The `listings.html` page displays a tile view of active donation listings. It also can display listings filtered to a specific category or only claimed donations.

- 	The `login.html` page provides a form for users to log in to their accounts.

- 	The `profile_page.html` page displays the user's profile information.

- 	The `register.html` page contains a form for users to create a new account.

- 	The `success.html` page is displayed after a successful monetary donation via Stripe and thanks the user for their support.

- 	The `admin.py` file contains configurations and settings related to the Django admin interface. It allows administrators to manage and interact with the application's data through a user-friendly interface.

- 	The `apps.py` file contains configuration settings for the individual Django apps within the project. It allows for customization and configuration specific to each app.

- 	The `forms.py` file contains a customized ‘NewListingForm’ form class that defines the structure and behavior of the form on the new listing page.

- 	The `models.py` file serves as the heart of the project, defining the application's data structure. It contains classes `User`, `Category` `Gender`, `ListingOffer`, `Price`, `Country`, and `Transaction` that map to database tables, including their fields and relationships. These models enable seamless interaction with the database, facilitating tasks such as data retrieval, manipulation, and storage. 

- 	The `urls.py` file serves as a router for mapping URL patterns to views or endpoints within the donation web application. It defines the URLs that users can access and specifies which views or functions should handle incoming requests to those URLs. This file plays a crucial role in directing the flow of web traffic within the application and is essential for defining the application's API endpoints, web pages, and other resources.

- 	The `views.py` contains Python functions or classes that handle incoming web requests and return appropriate HTTP responses. Views play a central role in implementing the business logic of the application and determining how users interact with it.

- 	The `requirements.txt` file contains packages required in order for the application to run successfully.

- The `settings.py` file serves as the configuration hub for Django project, encompassing various parameters that determine its behavior. It includes the Stripe API keys: STRIPE_PUBLIC_KEY and STRIPE_PRIVATE_KEY. These keys authenticate requests to Stripe's API, enabling secure and reliable payment transactions.

## How to Run the Application
1. Clone the repository to your system.

2. Install all project dependencies by running ‘pip install -r requirements.txt’.
- 	If you would like to use your own Stripe API keys, follow these steps:

            1.	Sign up for a Stripe account at Stripe.

            2.	Obtain your API keys from the Stripe Dashboard.

            3.	Install the stripe Python package using `pip install stripe`.

            4.	Insert the private and public keys from stripe developer dashboard in 'settings.py'.

3. Make and apply migrations by running `python manage.py makemigrations` and `python manage.py migrate`

4. Start the Django web server using `python manage.py runserver`.

5. Navigate to the website address and register for an account.

## Conclusion
    A big shoutout to the amazing team behind CS50's Web Programming with Python and JavaScript course! Your passion and commitment have inspired us all. Keep up the fantastic work! 😊
