(function ($) {
    "use strict";

    function refreshHidewhen() {
        var onsuccess = function(data, textStatus, xhr) {
            for (var hw in data)
                $('.hidewhen-' + hw).css('display', data[hw]?'none':'block');
        }
        
        $.ajax({
            type: 'POST',
            url: 'computehidewhens',
            data: $(this).closest('form').serialize(),
            success: onsuccess,
            dataType: 'json' 
        });
    };

    //Hidewhen without ajax call (only for single checkbox option)
    function simpleHidewhen() {
        $(".hidewhen-" + $(this).attr('data-dhw')).toggle();
    };


    $(function () {
        var elementName;
        $("input:checkbox[data-dhw = 1],input:radio[data-dhw = 1]").each(function(_,el){
            elementName = $(el).attr("name");
            $("input:checkbox[name = '" + elementName + "'],input:radio[name = '" + elementName + "']").on("change",refreshHidewhen);
        })
        $("input:text[data-dhw = 1],select[data-dhw = 1]").on("change",refreshHidewhen);
        $("input:checkbox[data-dhw]").not("[data-dhw = 1]").on("change",simpleHidewhen);

    });

})(jQuery);