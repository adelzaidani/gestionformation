$('#save_attendance').click(function(){
    var TableData;
    TableData = saveTable()
    TableData = $.toJSON(TableData);
        function saveTable(){
             var present='false';
                session=$('#num_session').val();
                TableData = new Array();
                date_selected=new Date($('#date_attendance').val());
                day = date_selected.getDate();
                month = date_selected.getMonth() + 1;
                year = date_selected.getFullYear();
                date_string=[year, month,day ].join('-');


               $('#table_attendance tr').each(function(row, tr){


                    if($(tr).find('td:eq(4) input:checked').is(':checked')){

                      present='1';
                    }
                    else{
                        present='2';
                    }

                     TableData[row]={
                        "id_client": $(tr).find('td:eq(0)').text()
                         ,"date":date_string
                         ,"attendance":present
                         ,"session":session

                     }

                });


        TableData.shift();
        return TableData;
        }

   var TableData;
       TableData = $.toJSON(saveTable());

         $.ajaxSetup({async: false});
         $.ajax({
            type: "POST",
            url: "/teacher/save_attendance/",
            data: "pTableData=" + TableData,
            success: function(data){
               if (data.exist) {
                    alert(data.message)
                }
                else{

                    alert(data.message);
                }

             }


         });




});

$('#date_attendance').change(function(){
    var date_selected;
        session=$('#num_session').val();

    date_selected=new Date($('#date_attendance').val())
    day = date_selected.getDate();
    month = date_selected.getMonth() + 1;
    year = date_selected.getFullYear();
    date_string=[year, month,day ].join('-');

    $.ajax({
        type:"POST",
        url:"/teacher/list_attendance/?id_session="+session+">",
        data:{'date_selected':date_selected},
        dataType:'Json',
        success:function(data){
            alert(data.message);

        }



    });

});

