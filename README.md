# SkyBound: Sky Adventure Hosting Platform

SkyBound is an innovative platform designed to streamline the booking and management of thrilling sky adventures such as skydiving, paragliding, and wingsuit jumps. Additionally, it offers professional certification courses like AFF (Accelerated Free Fall) and WSJC (Wingsuit Jumping Certification). This project features event management, course offerings, payment integration, and a blog application for user engagement and updates.

---

## Features

### **1. Event Management**
- **Event Listing:** View all upcoming sky adventure events with details.
- **Event Details:** Access comprehensive breakdowns including descriptions, itineraries, inclusions, exclusions, and pricing.
- **Event Registration:** Users can register for events and receive confirmation emails.
- **Capacity Management:** Tracks the maximum number of participants per event.

### **2. Course Offerings**
- **Professional Certifications:** View detailed course descriptions for AFF and WSJC.
- **Syllabus and Duration:** Comprehensive breakdowns of syllabus and timelines.
- **Dynamic Pricing:** Prices vary based on course levels and package details.
- **Registration:** Secure registration with email confirmations.

### **3. Payment Integration** (Powered by Razorpay)
- **Seamless Checkout:** Secure payments for events and courses.
- **Coupon System:** Apply discount codes during payment for offers.
- **Payment History:** Users can view their transaction history in their dashboards.

### **4. Blog Application**
- **Updates and Articles:** Read the latest articles about sky adventure tips, safety measures, and stories.
- **Interactive UI:** Engaging blog layout for easy readability.
- **Admin Management:** Blogs are easily manageable via the admin panel.

### **5. User Authentication**
- **Google Authentication:** Users can log in or sign up using their Google accounts.
- **Role-Based Access:** Different access levels for users, organizers, and admins.

### **6. Email Notifications**
- **Event Registration:** Confirmation emails with event details.
- **Payment Receipts:** Email receipts after successful payments.
- **Promotional Emails:** Updates about new events, courses, and offers.

### **7. Admin Panel**
- **Event and Course Management:** Create, update, or delete events and courses.
- **Blog Management:** Publish or manage blog posts.
- **User Insights:** View user registrations and payment details.

---

## Installation

### **1. Clone the Repository**
```bash
$ git clone https://github.com/username/skybound.git
$ cd skybound
```

### **2. Install Dependencies**
Create a virtual environment and install the required packages:
```bash
$ python -m venv venv
$ source venv/bin/activate  # For Linux/Mac
$ venv\Scripts\activate   # For Windows
$ pip install -r requirements.txt
```

### **3. Configure Environment Variables**
Create a `.env` file in the root directory with the following variables:
```
SECRET_KEY=<your_django_secret_key>
DEBUG=True
RAZORPAY_KEY_ID=<your_razorpay_key_id>
RAZORPAY_SECRET_KEY=<your_razorpay_secret_key>
EMAIL_HOST=<your_email_host>
EMAIL_PORT=<your_email_port>
EMAIL_HOST_USER=<your_email>
EMAIL_HOST_PASSWORD=<your_email_password>
GOOGLE_CLIENT_ID=<your_google_client_id>
GOOGLE_CLIENT_SECRET=<your_google_client_secret>
```

### **4. Apply Migrations**
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

### **5. Run the Server**
```bash
$ python manage.py runserver
```

---

## Usage

### **Event and Course Registration**
1. Navigate to the homepage to view available events and courses.
2. Click on an event or course to view details.
3. Register by filling out the form and completing the payment.
4. Receive a confirmation email with event/course details.

### **Google Authentication**
1. Click on the "Sign in with Google" button on the login page.
2. Authenticate using your Google account.
3. Access your personalized dashboard.

### **Coupon Redemption**
1. During payment, enter a valid coupon code in the provided field.
2. The total amount will adjust based on the discount.

### **Blogs**
1. Visit the blog section to read articles and updates.
2. Engage with the latest news on sky adventure trends.

---

## Technical Details

### **Technologies Used**
- **Backend:** Django, Django REST Framework
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** PostgreSQL
- **Authentication:** Google OAuth2 via Django-Allauth
- **Payment Gateway:** Razorpay
- **Email Service:** SMTP

### **Models Overview**
#### Event Model:
```python
class Event(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField()
    package = models.CharField(max_length=100)
    capacity = models.IntegerField()
    registration_amt = models.DecimalField(max_digits=10, decimal_places=2)
    price_details = models.DecimalField(max_digits=10, decimal_places=2)
    whats_included = RichTextField(blank=True, null=True)
    whats_not_included = RichTextField(blank=True, null=True)
    itinerary = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover_img = models.ImageField(upload_to='event/covers')
```

#### Course Model:
```python
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=100)
    syllabus = RichTextField(blank=True, null=True)
    cover_img = models.ImageField(upload_to='courses/covers', max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

---

## Future Enhancements
- **Dynamic Recommendations:** Suggest courses or events based on user interests.
- **Social Sharing:** Allow users to share event or course details on social media.
- **Multi-Language Support:** Enable content in multiple languages for global reach.
- **Advanced Analytics:** Provide detailed insights for admins on user activity.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact
For queries or support, email us at **Shubhamsurve30803@gmail.com**.

