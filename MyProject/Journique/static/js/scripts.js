function confirmDelete() {
            if (confirm("Are you sure you want to delete your profile? This action cannot be undone.")) {
                document.getElementById('edit-profile-form').action = "{% url 'delete_profile' %}";
                document.getElementById('edit-profile-form').submit();
            }
        }