function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#blah')
                .attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[0]);
    }s
}*/



window.onload = function(){

    //Check File API support
    if(window.File && window.FileList && window.FileReader)
    {
        var filesInput = document.getElementById("files");

        filesInput.addEventListener("change", function(event){

            var files = event.target.files; //FileList object
            var output = document.getElementById("result");

            for(var i = 0; i< files.length; i++)
            {
                var file = files[i];

                //Only pics
                if(!file.type.match('image'))
                  continue;

                var picReader = new FileReader();

                picReader.addEventListener("load",function(event){

                    var picFile = event.target;

                    var div = document.createElement("div");

                    div.innerHTML = "<img class='thumbnail' src='" + picFile.result + "'" +
                            "title='" + picFile.name + "'/>";

                    output.insertBefore(div,null);

                });

                 //Read the image
                picReader.readAsDataURL(file);
            }

        });
    }
    else
    {
        console.log("Your browser does not support File API");
    }
}




$( function() {
    $( "#datepicker" ).datepicker();
  } );


$( function() {
    $( "#datepicker2" ).datepicker2();
} );