// TES PALING DASAR
alert("JS TERHUBUNG");

document.addEventListener("DOMContentLoaded", function () {

  const surahSelect = document.getElementById("surahSelect");
  const content = document.getElementById("content");

  // TEST ISI MANUAL (tanpa API)
  surahSelect.innerHTML = `
    <option value="1">1. Al-Fatihah</option>
    <option value="2">2. Al-Baqarah</option>
  `;

  surahSelect.addEventListener("change", function () {
    content.innerHTML = `
      <p>Kamu memilih surah nomor: <b>${this.value}</b></p>
    `;
  });

});

