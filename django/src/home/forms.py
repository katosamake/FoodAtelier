from django.forms import ModelForm
from .models import Record
from .models import LabelTitle
from .models import LabelDetail


class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ["food_name","first_date","picture","memo","label_title1","label_title2",
        "label_title3","label_title4","label_title5","label_title6","label_title7",
        "label_title8"]

class LabelTitleForm(ModelForm):
    class Meta:
        model = LabelTitle
        fields = ["label_title_name"]

class LabelDetailForm(ModelForm):
    class Meta:
        model = LabelDetail
        fields = ["label_title_code","label_detail_name"]
        