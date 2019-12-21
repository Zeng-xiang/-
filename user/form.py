from django.forms import  ModelForm

from user.models import Profile

from django.forms import  ValidationError

class  ProfileModelForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def clean_max_distance(self):
        data = self.clean()
        min_distance = data['min_distance']
        max_distance = data['max_distance']
        if min_distance >= max_distance:
            raise ValidationError('min distance is qreate than max disintance')
        return max_distance

    def clean_max_dating_age(self):
        data = self.clean()
        min_dating_age = data['min_dating_age']
        max_dating_age = data['max_dating_age']
        if min_dating_age >= max_dating_age:
            raise ValidationError('最小年级不能大于最大年纪')
        return max_dating_age