// tootip初期化
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})

// toast初期化
let toastElList = [].slice.call(document.querySelectorAll(".toast"));
let toastList = toastElList.map(function (toastEl) {
    return new bootstrap.Toast(toastEl, {
        delay: 10000,
    });
});
toastElList[0].classList.add("hide")

// お知らせアイコンクリック処理
function onclickNoticeIcon() {
    let classList = document.querySelector("#noticeToast").classList

    if (classList.contains("show")) {
        toastList[0].hide();
    } else if (classList.contains("hide")) {
        toastList[0].show();
    } else {
        toastList[0].show();
    }
}
