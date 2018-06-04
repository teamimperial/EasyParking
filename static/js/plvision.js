/**
 * Created by Antonina on 18.05.2018.
 */

var Places;

/*

 http://easyparking.pythonanywhere.com/get/info/1

*/

$.ajax({
    url: "https://easyparking.pythonanywhere.com/get/info/1",
    type: "get",
    dataType: "json",
    async: false,

    success: function(data) {
        Places = data;
    }
});

console.log(Places);

var id_parking = Places.id_parking;

Places.places.forEach(function (item, i, Places) {
    id = id_parking + "." + item.id_line + "." + item.id_place;
    if (Number(item.status) === 0) {
        document.getElementById(id).style.backgroundColor = "#e83b3b";
    } else {
        document.getElementById(id).style.backgroundColor = "#90e26e";
    }
});