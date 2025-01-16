from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView,DetailView
from ..forms import RecordForm,LabelTitleForm,LabelDetailForm
from django.shortcuts import render,redirect,get_object_or_404
from ..models import LabelTitle,Record,LabelDetail
from django.views import View


class HomeView(TemplateView):
    def get(self, request):
        watch_list = Record.objects.order_by("-first_date")
        return render(request, "home/index.html",{"watch_list": watch_list})
template_name = "home/index.html"


class DesideView(TemplateView):
    template_name = "home/deside/deside.html"


class WatchListView(View):
    def get(self, request):
        watch_list = Record.objects.order_by("-first_date")
        # return render(request, "home/watch/watch.html",{"watch_list": watch_list})
        return render(request, "home/index.html",{"watch_list": watch_list})
watch_list = WatchListView.as_view()


class WatchDetailView(View):
    def get(self, request, id): 
        watch_detail = get_object_or_404(Record, id=id)
        return render(request, "home/watch/watch_detail.html", {"watch_detail": watch_detail})

watch_detail = WatchDetailView.as_view()

#料理を記録する
class RecordCreateView(TemplateView):
    def get(self, request):
        # 各ラベルを個別に取得
        label1 = get_object_or_404(LabelTitle, label_title_code="LT1")
        label2 = get_object_or_404(LabelTitle, label_title_code="LT2")
        label3 = get_object_or_404(LabelTitle, label_title_code="LT3")
        label4 = get_object_or_404(LabelTitle, label_title_code="LT4")
        label5 = get_object_or_404(LabelTitle, label_title_code="LT5")
        label6 = get_object_or_404(LabelTitle, label_title_code="LT6")
        label7 = get_object_or_404(LabelTitle, label_title_code="LT7")
        label8 = get_object_or_404(LabelTitle, label_title_code="LT8")
        form = RecordForm()
        return render(request, "home/record/record.html", {
            "form": form,
            "label1": label1,
            "label2": label2,
            "label3": label3,
            "label4": label4,
            "label5": label5,
            "label6": label6,
            "label7": label7,
            "label8": label8,
        })

    def post(self,request):
        form = RecordForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home:home")
        return render(request, "home/record/record.html",{"form": form})

record = RecordCreateView.as_view()


#記録した料理を編集する
class RecordUpdateView(View):
    def get(self,request, id):
        watch_detail = get_object_or_404(Record, id=id)
        form = RecordForm(instance=watch_detail)
        return render(request, "home/watch/watch_update.html",{"form": form})

    def post(self,request,id):
        watch_detail = get_object_or_404(Record, id=id)
        form = RecordForm(request.POST, request.FILES, instance=watch_detail)
        if form.is_valid():
            form.save()
            return redirect("home:record")
        return render(request, "home/record/record.html",{"form": form})

record_update = RecordUpdateView.as_view()


#記録した料理を削除する
class RecordDeleteView(View):
    def get(self,request, id):
        watch_detail = get_object_or_404(Record, id=id)
        return render(request, "home/watch/watch_delete_confirm.html", {"watch_detail": watch_detail})

    def post(self,request, id):
        watch_detail = get_object_or_404(Record, id=id)
        watch_detail.delete()
        return redirect("home:home")

record_delete = RecordDeleteView.as_view()


#親ラベルを登録する
class RecordLabelTitleView(TemplateView):
    def get(self,request):
        form = LabelTitleForm()
        return render(request, "home/record/record_edit.html",{"form": form})

    def post(self,request):
        form = LabelTitleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:record_edit")
        return render(request, "home/record/record_edit.html",{"form": form})

record_edit = RecordLabelTitleView.as_view()


#ラベル編集ページで親ラベルを表示させる
class RecordListView(View):
    def get(self,request):
        label_list = LabelTitle.objects.all()
        return render(request, "home/record/record_label.html",{"label_list": label_list})

record_label = RecordListView.as_view()


#親ラベルを更新する
class RecordLabelUpdateView(TemplateView):
    def get(self,request,id):
        label_title = get_object_or_404(LabelTitle, id=id)
        form = LabelTitleForm(instance=label_title)
        return render(request, "home/record/record_label_update.html",{"form": form})
        
    def post(self,request,id):
        label_title = get_object_or_404(LabelTitle, id=id)
        form = LabelTitleForm(request.POST,request.FILES,instance=label_title)
        if form.is_valid():
            form.save()
            return redirect("home:record_label")
        return render(request, "home/record/record_label_update.html",{"form": form})

record_label_update = RecordLabelUpdateView.as_view()


#子ラベルを登録する
class RecordLabelDetailView(TemplateView):
    def get(self,request):
        form = LabelDetailForm()
        return render(request, "home/record/record_edit_detail.html",{"form": form})

    def post(self,request):
        form = LabelDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:record_edit_detail")
        return render(request, "home/record/record_edit_detail.html",{"form": form})

record_edit_detail = RecordLabelDetailView.as_view()


#子ラベルを更新する
class RecordLabelDetailUpdateView(TemplateView):
    def get(self,request,id):
        label_detail = get_object_or_404(LabelDetail, id=id)
        form = LabelDetailForm(instance=label_detail)
        return render(request, "home/record/record_label_detail_update.html",{"form": form})
        
    def post(self,request,id):
        label_detail = get_object_or_404(LabelDetail, id=id)
        form = LabelDetailForm(request.POST,request.FILES,instance=label_detail)
        if form.is_valid():
            form.save()
            return redirect("home:record_label")
        return render(request, "home/record/record_label_detail_update.html",{"form": form})

record_label_detail_update = RecordLabelDetailUpdateView.as_view()


#ラベル編集ページで親ラベルに関連する子ラベルを表示させる
class RecordDetailDetailView(View):
    def get(self,request,label_title_code_id):
        label_detail = LabelDetail.objects.filter(label_title_code=label_title_code_id)
        return render(request,"home/record/record_label_detail.html",{"label_detail": label_detail})

record_label_detail = RecordDetailDetailView.as_view()