from django.contrib import admin
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
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
    SportPhoto,
    SportVideo,
    AdmissionApplication,
)


# ============================================================
# SCHOOL SETTINGS
# ============================================================

@admin.register(SchoolSettings)
class SchoolSettingsAdmin(admin.ModelAdmin):

    list_display = (
        "school_name",
        "phone",
        "email",
        "whatsapp_number",
        "admission_open",
        "admission_button_show",
    )

    search_fields = (
        "school_name",
        "phone",
        "email",
        "whatsapp_number",
    )

    list_filter = (
        "admission_open",
        "admission_button_show",
    )


# ============================================================
# PRINCIPAL
# ============================================================

@admin.register(Principal)
class PrincipalAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "designation",
        "is_active",
    )

    search_fields = (
        "name",
        "designation",
    )

    list_filter = (
        "is_active",
    )


# ============================================================
# HOME PHOTOS
# ============================================================

@admin.register(HomePhoto)
class HomePhotoAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "order",
        "is_active",
    )

    search_fields = (
        "title",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "order",
        "-id",
    )


# ============================================================
# GALLERY PHOTOS
# ============================================================

@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "order",
        "is_active",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    ordering = (
        "order",
        "-created_at",
    )


# ============================================================
# GALLERY VIDEOS
# ============================================================

@admin.register(GalleryVideo)
class GalleryVideoAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "order",
        "is_active",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    ordering = (
        "order",
        "-created_at",
    )


# ============================================================
# RESULTS
# ============================================================

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):

    list_display = (
        "student_name",
        "student_class",
        "percentage",
        "year",
        "rank",
        "is_active",
    )

    search_fields = (
        "student_name",
    )

    list_filter = (
        "student_class",
        "year",
        "is_active",
    )

    ordering = (
        "student_class",
        "-percentage",
    )


# ============================================================
# ABOUT SCHOOL
# ============================================================

@admin.register(AboutSchool)
class AboutSchoolAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "is_active",
    )

    search_fields = (
        "title",
        "content",
    )

    list_filter = (
        "is_active",
    )


# ============================================================
# FACILITIES
# ============================================================

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "order",
        "is_active",
    )

    search_fields = (
        "title",
        "description",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "order",
        "-id",
    )


# ============================================================
# ACADEMICS
# ============================================================

@admin.register(Academic)
class AcademicAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "order",
        "is_active",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    ordering = (
        "order",
        "-created_at",
    )


# ============================================================
# SPORTS
# ============================================================

@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "order",
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
        "description",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    ordering = (
        "order",
        "-created_at",
    )


# ============================================================
# SPORT PHOTOS
# ============================================================

@admin.register(SportPhoto)
class SportPhotoAdmin(admin.ModelAdmin):

    list_display = (
        "sport",
        "title",
        "order",
        "is_active",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
        "sport__name",
    )

    list_filter = (
        "sport",
        "is_active",
        "created_at",
    )

    ordering = (
        "order",
        "-created_at",
    )


# ============================================================
# SPORT VIDEOS
# ============================================================

@admin.register(SportVideo)
class SportVideoAdmin(admin.ModelAdmin):

    list_display = (
        "sport",
        "title",
        "order",
        "is_active",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
        "sport__name",
    )

    list_filter = (
        "sport",
        "is_active",
        "created_at",
    )

    ordering = (
        "order",
        "-created_at",
    )


# ============================================================
# ADMISSION APPLICATION
# ============================================================

@admin.register(AdmissionApplication)
class AdmissionApplicationAdmin(admin.ModelAdmin):

    list_display = (
        "application_number",
        "student_name",
        "father_name",
        "applying_class",
        "mobile",
        "email",
        "status",
        "submitted_at",
    )

    search_fields = (
        "application_number",
        "student_name",
        "father_name",
        "mother_name",
        "mobile",
        "email",
        "applying_class",
    )

    list_filter = (
        "status",
        "applying_class",
        "gender",
        "submitted_at",
    )

    readonly_fields = (
        "application_number",
        "submitted_at",
    )

    ordering = (
        "-submitted_at",
    )

    # ========================================================
    # SAVE MODEL
    # ========================================================

    def save_model(
        self,
        request,
        obj,
        form,
        change
    ):

        old_status = None

        if change and obj.pk:

            try:

                old_obj = AdmissionApplication.objects.get(
                    pk=obj.pk
                )

                old_status = old_obj.status

            except AdmissionApplication.DoesNotExist:

                old_status = None

        # ----------------------------------------------------
        # SAVE DATABASE FIRST
        # ----------------------------------------------------

        super().save_model(
            request,
            obj,
            form,
            change
        )

        # ----------------------------------------------------
        # NO USER EMAIL
        # ----------------------------------------------------

        if not obj.email:
            return

        # ----------------------------------------------------
        # SAME STATUS = NO EMAIL
        # ----------------------------------------------------

        if old_status == obj.status:
            return

        # ----------------------------------------------------
        # SCHOOL SETTINGS
        # ----------------------------------------------------

        school = SchoolSettings.objects.first()

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
            else settings.EMAIL_HOST_USER
        )

        # ----------------------------------------------------
        # ESCAPE DATA
        # ----------------------------------------------------

        student_name = escape(obj.student_name)
        father_name = escape(obj.father_name)
        applying_class = escape(obj.applying_class)

        # IMPORTANT:
        # Application ID ki jagah Application Number
        application_number = escape(
            obj.application_number
        )

        # ----------------------------------------------------
        # STATUS DETAILS
        # ----------------------------------------------------

        subject = None
        heading = None
        message_text = None
        status_color = "#2563eb"

        if obj.status == "Contacted":

            subject = (
                f"Admission Application Update - "
                f"{obj.student_name}"
            )

            heading = "Application Under Review"

            message_text = (
                "Your admission application has been "
                "received and reviewed by our school team. "
                "Our school representative may contact "
                "you shortly regarding the next steps."
            )

            status_color = "#2563eb"

        elif obj.status == "Approved":

            subject = (
                f"Admission Application Approved - "
                f"{obj.student_name}"
            )

            heading = "Admission Application Approved"

            message_text = (
                "Congratulations! We are pleased to inform "
                "you that your admission application has "
                "been approved by the school."
            )

            status_color = "#16a34a"

        elif obj.status == "Rejected":

            subject = (
                f"Admission Application Status - "
                f"{obj.student_name}"
            )

            heading = "Admission Application Update"

            message_text = (
                "Thank you for applying for admission to "
                "our school. After reviewing the application, "
                "we regret to inform you that the application "
                "has not been accepted at this time."
            )

            status_color = "#dc2626"

        else:
            return

        # ====================================================
        # LOGO AVAILABILITY
        # ====================================================

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

        # ====================================================
        # LOGO HTML
        # ====================================================

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

        # ====================================================
        # HTML EMAIL
        # ====================================================

        html_message = f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width,
               initial-scale=1.0">

<title>{heading}</title>

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
    width="650"
    cellpadding="0"
    cellspacing="0"
    border="0"
    style="
        max-width:650px;
        width:100%;
        background:#ffffff;
        border-radius:18px;
        overflow:hidden;
        box-shadow:0 8px 30px rgba(0,0,0,0.08);
    "
>

<!-- ================================================== -->
<!-- HEADER -->
<!-- ================================================== -->

<tr>

<td
    align="center"
    style="
        background:#2563eb;
        padding:30px 25px;
        color:#ffffff;
    "
>

{logo_html}

<div style="
    font-size:25px;
    font-weight:700;
    line-height:1.3;
">

    {escape(school_name)}

</div>

<div style="
    font-size:13px;
    margin-top:8px;
    opacity:0.92;
">

    Admission Department

</div>

</td>

</tr>


<!-- ================================================== -->
<!-- STATUS -->
<!-- ================================================== -->

<tr>

<td style="
    padding:30px 30px 15px 30px;
">

<div style="
    background:{status_color};
    color:#ffffff;
    padding:16px 20px;
    border-radius:12px;
    text-align:center;
    font-size:20px;
    font-weight:700;
">

{heading}

</div>

</td>

</tr>


<!-- ================================================== -->
<!-- MESSAGE -->
<!-- ================================================== -->

<tr>

<td style="
    padding:10px 30px 20px 30px;
">

<p style="
    margin:0 0 10px 0;
    font-size:17px;
    color:#111827;
">

    Dear <strong>{student_name}</strong>,

</p>

<p style="
    margin:0;
    font-size:15px;
    line-height:1.8;
    color:#4b5563;
">

    {message_text}

</p>

</td>

</tr>


<!-- ================================================== -->
<!-- APPLICATION DETAILS -->
<!-- ================================================== -->

<tr>

<td style="
    padding:10px 30px 25px 30px;
">

<div style="
    font-size:18px;
    font-weight:700;
    color:#111827;
    margin-bottom:15px;
">

    Application Details

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
    padding:13px;
    background:#f8fafc;
    width:45%;
    font-weight:600;
    color:#475569;
">

Student Name

</td>

<td style="
    padding:13px;
    color:#111827;
">

{student_name}

</td>

</tr>


<tr>

<td style="
    padding:13px;
    background:#f8fafc;
    font-weight:600;
    color:#475569;
">

Father's Name

</td>

<td style="
    padding:13px;
    color:#111827;
">

{father_name}

</td>

</tr>


<tr>

<td style="
    padding:13px;
    background:#f8fafc;
    font-weight:600;
    color:#475569;
">

Applying Class

</td>

<td style="
    padding:13px;
    color:#111827;
">

{applying_class}

</td>

</tr>


<tr>

<td style="
    padding:13px;
    background:#f8fafc;
    font-weight:600;
    color:#475569;
">

Application Number

</td>

<td style="
    padding:13px;
    color:#111827;
    font-weight:700;
">

{application_number}

</td>

</tr>

</table>

</td>

</tr>


<!-- ================================================== -->
<!-- CONTACT -->
<!-- ================================================== -->

<tr>

<td style="
    padding:5px 30px 30px 30px;
">

<div style="
    background:#eff6ff;
    border-radius:12px;
    padding:20px;
">

<div style="
    font-size:16px;
    font-weight:700;
    color:#1e3a8a;
    margin-bottom:10px;
">

Need Help?

</div>

<div style="
    font-size:14px;
    line-height:1.7;
    color:#475569;
">

Please contact the school administration if you
need any clarification regarding your application.

<br><br>

{f"Phone: {escape(school_phone)}" if school_phone else ""}

<br>

Email: {escape(school_email)}

</div>

</div>

</td>

</tr>


<!-- ================================================== -->
<!-- FOOTER -->
<!-- ================================================== -->

<tr>

<td
    align="center"
    style="
        background:#0f172a;
        padding:25px 20px;
        color:#ffffff;
    "
>

<div style="
    font-size:15px;
    font-weight:700;
">

{escape(school_name)}

</div>

<div style="
    font-size:12px;
    color:#cbd5e1;
    margin-top:7px;
">

School Administration

</div>

<div style="
    font-size:11px;
    color:#94a3b8;
    margin-top:12px;
">

This is an automated email from the school website.
Please do not reply to this automated notification.

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

        # ====================================================
        # PLAIN TEXT FALLBACK
        # ====================================================

        plain_message = f"""
{school_name}

{heading}

Dear {obj.student_name},

{message_text}


APPLICATION DETAILS

Student Name: {obj.student_name}
Father's Name: {obj.father_name}
Applying Class: {obj.applying_class}
Application Number: {obj.application_number}


Please contact the school administration if you
need any clarification.

Phone: {school_phone}
Email: {school_email}


Regards,

{school_name}
School Administration
"""

        # ====================================================
        # CREATE EMAIL
        # ====================================================

        email = EmailMultiAlternatives(
            subject=subject,
            body=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            to=[obj.email],
            reply_to=[
                settings.EMAIL_HOST_USER
            ],
        )

        # ====================================================
        # ATTACH HTML
        # ====================================================

        email.attach_alternative(
            html_message,
            "text/html"
        )

        # ====================================================
        # ATTACH SCHOOL LOGO INLINE
        # ====================================================

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

                email.attach(
                    logo_image
                )

            except Exception:

                pass

        # ====================================================
        # SEND EMAIL
        # ====================================================

        email.send(
            fail_silently=False
        )