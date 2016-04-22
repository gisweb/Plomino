(function ($) {
    "use strict";

    function refreshHidewhen() {
        var $element = $(this)
        var onsuccess = function(data, textStatus, xhr) {
            for (var hw in data){
                var $hw = $element.closest('form').find('.hidewhen-' + hw)
                $hw.css('display', data[hw]?'none':'block');
            }
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
        //$(".hidewhen-" + $(this).attr('data-dhw')).toggle();
        hw = ".hidewhen-" + $(this).attr('data-dhw')
        $(this).closest('form').find(hw).toggle();
    };

    function toggleHidewhen(){
        var elementName;
        $("input:checkbox[data-dhw = 1],input:radio[data-dhw = 1]").each(function(_,el){
            elementName = $(el).attr("name");
            $("input:checkbox[name = '" + elementName + "'],input:radio[name = '" + elementName + "']").on("change",refreshHidewhen);
        })
        $("input:text[data-dhw = 1],select[data-dhw = 1]").on("change",refreshHidewhen);
        $("input:checkbox[data-dhw]").not("[data-dhw = 1]").on("change",simpleHidewhen);
    }

    $(function () {
        toggleHidewhen();
    });

    //INIZIALIZZO TUTTO IL CONTENUTO DEL DIALOG DOPO AVER APERTO IL DIALOG DEL DATAGRID
    $(document).on('opendialog',function(_, container){
        toggleHidewhen();
    });



})(jQuery);