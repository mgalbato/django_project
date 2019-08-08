$(document).ready(function() {
    var temp = context_var.substring(2, context_var.length - 2);
    var cities = temp.split("', '")
    $('#city').selectivity({
        allowClear: true,
        items: cities,
        placeholder: 'Where do you live?',
        required: true
    });
});
