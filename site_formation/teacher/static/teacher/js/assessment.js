$('.assessment').change(function(){
    var total=0;
        i=0;
        val=0;
    $('.assessment').each(function(){
        val= $('.assessment').val();
        total+=val;
        i+=1;


    });
    alert(total);


});

