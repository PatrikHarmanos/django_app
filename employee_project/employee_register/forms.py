from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('fullname', 'emp_code', 'mobile', 'position')
        labels = {
            'fullname': 'Full Name',
            'emp_code': 'EMP. Code'
        }

    # delete --- from positions combo box and add placeholder
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        # self.fields['mobile'].required = False
