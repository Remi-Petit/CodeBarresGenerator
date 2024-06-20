document.getElementById("capture-btn").addEventListener("click", function() {

    // Élément à mettre en image
    var htmlToImage = document.getElementsByClassName("container-table")[0];

    html2canvas(htmlToImage).then(function(canvas) {
      // Créer un élément <a> pour télécharger l'image
      var link = document.createElement('a');
      link.href = canvas.toDataURL();
      link.download = 'etiquettes_'+numero_de_depart+'_a_'+numero_de_fin+'.png';
      link.click();
    });
});