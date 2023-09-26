from django.contrib.auth.decorators import user_passes_test

def is_it_staff(user):
    return user.groups.filter(name="IT Support").exists()

it_staff_required = user_passes_test(is_it_staff)
