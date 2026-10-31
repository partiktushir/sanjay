from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.utils.html import escape

from email.mime.image import MIMEImage

from .models import (
    SchoolSettings,
    Principal,
    HomePhoto,
    GalleryPhoto,
    GalleryVideo,
    Result,
    AboutSchool,
    Facility,
    Academic,
    Sport,
)

from .forms import AdmissionApplicationForm


# ==========================================================
# SCHOOL SETTINGS
# ==========================================================

def get_school_settings():

    return SchoolSettings.objects.first()


# ==========================================================
# HOME
# ==========================================================

def home(request):

    school = get_school_settings()

    principal = Principal.objects.filter(
        is_active=True
    ).first()

    home_photos = HomePhoto.objects.filter(
        is_active=True
    )

    # ------------------------------------------------------
    # GOOGLE MAP LOCATION
    # ------------------------------------------------------

    location_embed_url = ""

    if school:

        location_embed_url = (
            school.location_embed_url or ""
        ).strip()

    location_url = ""

    if school:

        location_url = (
            school.location_url or ""
        ).strip()

    return render(
        request,
        "home.html",
        {
            "school": school,
            "principal": principal,
            "home_photos": home_photos,
            "location_embed_url": location_embed_url,
            "location_url": location_url,
        }
    )


# ==========================================================
# GALLERY
# ==========================================================

def gallery(request):

    school = get_school_settings()

    photos = GalleryPhoto.objects.filter(
        is_active=True
    )

    videos = GalleryVideo.objects.filter(
        is_active=True
    )

    return render(
        request,
        "gallery.html",
        {
            "school": school,
            "photos": photos,
            "videos": videos,
        }
    )


# ==========================================================
# RESULT
# ==========================================================

def result(request):

    school = get_school_settings()

    results = Result.objects.filter(
        is_active=True
    )

    return render(
        request,
        "result.html",
        {
            "school": school,
            "results": results,
        }
    )


# ==========================================================
# ABOUT
# ==========================================================

def about(request):

    school = get_school_settings()

    about_school = AboutSchool.objects.filter(
        is_active=True
    ).first()

    facilities = Facility.objects.filter(
        is_active=True
    )

    return render(
        request,
        "about.html",
        {
            "school": school,
            "about_school": about_school,
            "facilities": facilities,
        }
    )


# ==========================================================
# ADMISSION
# ==========================================================

def admission(request):

    school = get_school_settings()

    if request.method == "POST":

        form = AdmissionApplicationForm(
            request.POST
        )

        if form.is_valid():

            # ------------------------------------------------
            # SAVE APPLICATION
            # ------------------------------------------------

            application = form.save()

            # ------------------------------------------------
            # SCHOOL INFORMATION
            # ------------------------------------------------

            school_name = (
                school.school_name
                if school
                else "School Administration"
            )

            school_phone = (
                school.phone
                if school and school.phone
                else ""
            )

            school_email = (
                school.email
                if school and school.email
                else settings.ADMISSION_EMAIL
            )

            # ------------------------------------------------
            # APPLICATION NUMBER
            # ------------------------------------------------

            application_number = escape(
                application.application_number
            )

            # ------------------------------------------------
            # SAFE DATA
            # ------------------------------------------------

            student_name = escape(
                application.student_name
            )

            father_name = escape(
                application.father_name
            )

            mother_name = (
                escape(
                    application.mother_name
                )
                if application.mother_name
                else "Not Provided"
            )

            # ------------------------------------------------
            # DATE OF BIRTH
            # ------------------------------------------------

            if application.date_of_birth:

                dob = escape(
                    application.date_of_birth.strftime(
                        "%d-%m-%Y"
                    )
                )

            else:

                dob = "Not Provided"

            # ------------------------------------------------
            # GENDER
            # ------------------------------------------------

            gender = (
                escape(
                    application.gender
                )
                if application.gender
                else "Not Provided"
            )

            applying_class = escape(
                application.applying_class
            )

            mobile = escape(
                application.mobile
            )

            email_address = (
                escape(
                    application.email
                )
                if application.email
                else "Not Provided"
            )

            # ------------------------------------------------
            # ADDRESS
            # ------------------------------------------------

            address = escape(
                application.address
            ).replace(
                "\n",
                "<br>"
            )

            # ------------------------------------------------
            # PREVIOUS SCHOOL
            # ------------------------------------------------

            previous_school = (
                escape(
                    application.previous_school
                )
                if application.previous_school
                else "Not Provided"
            )

            # ------------------------------------------------
            # ADDITIONAL MESSAGE
            # ------------------------------------------------

            additional_message = (
                escape(
                    application.message
                ).replace(
                    "\n",
                    "<br>"
                )
                if application.message
                else "No additional message"
            )

            # ------------------------------------------------
            # SUBJECT
            # ------------------------------------------------

            subject = (
                f"🎓 New Admission Application - "
                f"{application.student_name}"
            )

            # =================================================
            # CHECK SCHOOL LOGO
            # =================================================

            logo_available = False
            logo_data = None

            if school and school.logo:

                try:

                    with open(
                        school.logo.path,
                        "rb"
                    ) as logo_file:

                        logo_data = logo_file.read()

                    if logo_data:

                        logo_available = True

                except Exception:

                    logo_available = False
                    logo_data = None

            # =================================================
            # LOGO HTML
            # =================================================

            logo_html = ""

            if logo_available:

                logo_html = """
                <img
                    src="cid:school_logo"
                    alt="School Logo"
                    width="90"
                    style="
                        width:90px;
                        max-width:90px;
                        height:auto;
                        max-height:90px;
                        display:block;
                        margin:0 auto 12px auto;
                        border-radius:12px;
                    "
                >
                """

            # =================================================
            # HTML EMAIL
            # =================================================

            html_message = f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width,
               initial-scale=1.0">

<title>New Admission Application</title>

</head>


<body style="
    margin:0;
    padding:0;
    background:#f1f5f9;
    font-family:Arial, Helvetica, sans-serif;
">


<table
    width="100%"
    cellpadding="0"
    cellspacing="0"
    border="0"
    style="background:#f1f5f9;"
>


<tr>

<td
    align="center"
    style="padding:30px 15px;"
>


<table
    width="700"
    cellpadding="0"
    cellspacing="0"
    border="0"
    style="
        width:100%;
        max-width:700px;
        background:#ffffff;
        border-radius:18px;
        overflow:hidden;
        box-shadow:0 8px 30px rgba(0,0,0,0.08);
    "
>


<!-- ===================================================== -->
<!-- HEADER -->
<!-- ===================================================== -->

<tr>

<td
    align="center"
    style="
        background:#2563eb;
        padding:32px 25px;
        color:#ffffff;
    "
>


{logo_html}


<div style="
    font-size:28px;
    font-weight:700;
    line-height:1.3;
">

    {escape(school_name)}

</div>


<div style="
    margin-top:8px;
    font-size:14px;
    color:#dbeafe;
">

    Admission Department

</div>


</td>

</tr>


<!-- ===================================================== -->
<!-- TITLE -->
<!-- ===================================================== -->

<tr>

<td
    style="
        padding:30px 30px 15px 30px;
    "
>


<div style="
    background:#eff6ff;
    border-left:6px solid #2563eb;
    padding:20px;
    border-radius:10px;
">


<div style="
    font-size:24px;
    font-weight:700;
    color:#1e3a8a;
">

New Admission Application

</div>


<div style="
    margin-top:8px;
    font-size:14px;
    color:#64748b;
">

A new admission form has been submitted
through the school website.

</div>


</div>

</td>

</tr>


<!-- ===================================================== -->
<!-- STUDENT INFORMATION -->
<!-- ===================================================== -->

<tr>

<td style="padding:15px 30px;">


<div style="
    font-size:19px;
    font-weight:700;
    color:#111827;
    margin-bottom:15px;
">

👨‍🎓 Student Information

</div>


<table
    width="100%"
    cellpadding="0"
    cellspacing="0"
    border="0"
    style="
        border:1px solid #e5e7eb;
        border-radius:12px;
        overflow:hidden;
    "
>


<tr>

<td style="
    width:42%;
    padding:14px;
    background:#f8fafc;
    font-weight:600;
    color:#475569;
">

Student Name

</td>

<td style="
    padding:14px;
    color:#111827;
    font-weight:600;
">

{student_name}

</td>

</tr>


<tr>

<td style="
    padding:14px;
    background:#f8fafc;
    font-weight:600;
    color:#475569;
">

Father's Name

</td>

<td style="
    padding:14px;
    color:#111827;
">

{father_name}

</td>

</tr>


<tr>

<td style="
    padding:14px;
    background:#f8fafc;
    font-weight:600;
    color:#475569;
">

Mother's Name

</td>

<td style="
    padding:14px;
    color:#111827;
">

{mother_name}

</td>

</tr>


<tr>

<td style="
    padding:14px;
    background:#f8fafc;
    font-weight:600;
    color:#475569;
">

Date of Birth

</td>

<td style="
    padding:14px;
    color:#111827;
">

{dob}

</td>

</tr>


<tr>

<td style="
    padding:14px;
    background:#f8fafc;
    font-weight:600;
    color:#475569;
">

Gender

</td>

<td style="
    padding:14px;
    color:#111827;
">

{gender}

</td>

</tr>


<tr>

<td style="
    padding:14px;
    background:#f8fafc;
    font-weight:600;
    color:#475569;
">

Applying Class

</td>

<td style="
    padding:14px;
    color:#111827;
    font-weight:600;
">

{applying_class}

</td>

</tr>


</table>

</td>

</tr>


<!-- ===================================================== -->
<!-- CONTACT INFORMATION -->
<!-- ===================================================== -->

<tr>

<td style="padding:15px 30px;">


<div style="
    font-size:19px;
    font-weight:700;
    color:#111827;
    margin-bottom:15px;
">

📞 Contact Information

</div>


<table
    width="100%"
    cellpadding="0"
    cellspacing="0"
    border="0"
    style="
        border:1px solid #e5e7eb;
        border-radius:12px;
        overflow:hidden;
    "
>


<tr>

<td style="
    width:42%;
    padding:14px;
    background:#f8fafc;
    font-weight:600;
    color:#475569;
">

Mobile Number

</td>

<td style="
    padding:14px;
    color:#111827;
    font-weight:600;
">

{mobile}

</td>

</tr>


<tr>

<td style="
    padding:14px;
    background:#f8fafc;
    font-weight:600;
    color:#475569;
">

Email Address

</td>

<td style="
    padding:14px;
    color:#111827;
">

{email_address}

</td>

</tr>


<tr>

<td style="
    padding:14px;
    background:#f8fafc;
    font-weight:600;
    color:#475569;
">

Address

</td>

<td style="
    padding:14px;
    color:#111827;
    line-height:1.6;
">

{address}

</td>

</tr>


</table>

</td>

</tr>


<!-- ===================================================== -->
<!-- PREVIOUS SCHOOL -->
<!-- ===================================================== -->

<tr>

<td style="padding:15px 30px;">


<div style="
    background:#f8fafc;
    border:1px solid #e5e7eb;
    border-radius:12px;
    padding:20px;
">


<div style="
    font-size:16px;
    font-weight:700;
    color:#334155;
    margin-bottom:8px;
">

🏫 Previous School

</div>


<div style="
    font-size:15px;
    color:#475569;
">

{previous_school}

</div>


</div>

</td>

</tr>


<!-- ===================================================== -->
<!-- MESSAGE -->
<!-- ===================================================== -->

<tr>

<td style="padding:15px 30px;">


<div style="
    background:#fffbeb;
    border:1px solid #fde68a;
    border-radius:12px;
    padding:20px;
">


<div style="
    font-size:16px;
    font-weight:700;
    color:#92400e;
    margin-bottom:8px;
">

💬 Additional Message

</div>


<div style="
    font-size:15px;
    line-height:1.7;
    color:#57534e;
">

{additional_message}

</div>


</div>

</td>

</tr>


<!-- ===================================================== -->
<!-- APPLICATION INFORMATION -->
<!-- ===================================================== -->

<tr>

<td style="padding:15px 30px 30px 30px;">


<div style="
    background:#ecfdf5;
    border:1px solid #bbf7d0;
    border-radius:12px;
    padding:20px;
">


<div style="
    font-size:17px;
    font-weight:700;
    color:#166534;
    margin-bottom:12px;
">

📋 Application Information

</div>


<div style="
    font-size:14px;
    line-height:2;
    color:#166534;
">


<strong>Application Number:</strong>

{application_number}


<br>


<strong>Submitted At:</strong>

{application.submitted_at}


<br>


<strong>Status:</strong>

New


</div>


</div>

</td>

</tr>


<!-- ===================================================== -->
<!-- FOOTER -->
<!-- ===================================================== -->

<tr>

<td
    align="center"
    style="
        background:#0f172a;
        padding:28px 20px;
        color:#ffffff;
    "
>


<div style="
    font-size:16px;
    font-weight:700;
">

{escape(school_name)}

</div>


<div style="
    margin-top:7px;
    font-size:12px;
    color:#cbd5e1;
">

Admission Department

</div>


<div style="
    margin-top:12px;
    font-size:11px;
    color:#94a3b8;
">

This application was submitted through the
official school website.

</div>


</td>

</tr>


</table>

</td>

</tr>

</table>


</body>

</html>
"""

            # =================================================
            # PLAIN TEXT FALLBACK
            # =================================================

            email_body = f"""
NEW ADMISSION APPLICATION

{school_name}
Admission Department

----------------------------------------

STUDENT INFORMATION

Student Name:
{application.student_name}

Father's Name:
{application.father_name}

Mother's Name:
{application.mother_name or "Not Provided"}

Date of Birth:
{application.date_of_birth or "Not Provided"}

Gender:
{application.gender or "Not Provided"}

Applying Class:
{application.applying_class}


----------------------------------------

CONTACT INFORMATION

Mobile:
{application.mobile}

Email:
{application.email or "Not Provided"}

Address:
{application.address}


----------------------------------------

PREVIOUS SCHOOL

{application.previous_school or "Not Provided"}


----------------------------------------

ADDITIONAL MESSAGE

{application.message or "No additional message"}


----------------------------------------

APPLICATION INFORMATION

Application Number:
{application.application_number}

Submitted At:
{application.submitted_at}

Status:
New


----------------------------------------

{school_name}
Admission Department
"""

            # =================================================
            # CREATE EMAIL
            # =================================================

            email_message = EmailMultiAlternatives(
                subject=subject,
                body=email_body,
                from_email=settings.EMAIL_HOST_USER,
                to=[
                    settings.ADMISSION_EMAIL
                ],
                reply_to=(
                    [application.email]
                    if application.email
                    else None
                ),
            )

            # =================================================
            # HTML VERSION
            # =================================================

            email_message.attach_alternative(
                html_message,
                "text/html"
            )

            # =================================================
            # ATTACH SCHOOL LOGO INLINE
            # =================================================

            if logo_available and logo_data:

                try:

                    logo_image = MIMEImage(
                        logo_data
                    )

                    logo_image.add_header(
                        "Content-ID",
                        "<school_logo>"
                    )

                    logo_image.add_header(
                        "Content-Disposition",
                        "inline",
                        filename="school-logo"
                    )

                    email_message.attach(
                        logo_image
                    )

                except Exception:

                    pass

            # =================================================
            # SEND EMAIL
            # =================================================

            email_message.send(
                fail_silently=False
            )

            # ------------------------------------------------
            # SUCCESS
            # ------------------------------------------------

            return redirect(
                "admission_success"
            )

    else:

        form = AdmissionApplicationForm()

    return render(
        request,
        "admission.html",
        {
            "school": school,
            "form": form,
        }
    )


# ==========================================================
# ADMISSION SUCCESS
# ==========================================================

def admission_success(request):

    school = get_school_settings()

    return render(
        request,
        "admission_success.html",
        {
            "school": school,
        }
    )


# ==========================================================
# FACILITIES
# ==========================================================

def facilities(request):

    school = get_school_settings()

    facilities = Facility.objects.filter(
        is_active=True
    ).order_by(
        "order",
        "-id"
    )

    return render(
        request,
        "facilities.html",
        {
            "school": school,
            "facilities": facilities,
        }
    )


# ==========================================================
# ACADEMICS
# ==========================================================

def academics(request):

    school = get_school_settings()

    academics = Academic.objects.filter(
        is_active=True
    ).order_by(
        "order",
        "-id"
    )

    return render(
        request,
        "academics.html",
        {
            "school": school,
            "academics": academics,
        }
    )


# ==========================================================
# SPORTS
# ==========================================================

def sports(request):

    school = get_school_settings()

    sports_list = Sport.objects.filter(
        is_active=True
    ).prefetch_related(
        "photos",
        "videos"
    ).order_by(
        "order",
        "-id"
    )

    return render(
        request,
        "sports.html",
        {
            "school": school,
            "sports_list": sports_list,
        }
    )