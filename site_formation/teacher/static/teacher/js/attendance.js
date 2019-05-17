$('#save_attendance').click(function(){
    var TableData;
    TableData = saveTable()
    TableData = $.toJSON(TableData);
        function saveTable(){
             var present='false';
                session=$('#num_session').val();
                TableData = new Array();
                date_selected=new Date($('#start_date').val());
                day = date_selected.getDate();
                month = date_selected.getMonth() + 1;
                year = date_selected.getFullYear();
                date_string=[day, month, year].join('/');

               $('#table_attendance tr').each(function(row, tr){


                    if($(tr).find('td:eq(4) input:checked').is(':checked')){

                      present='true';
                    }
                    else{
                        present='false';
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


         $.ajax({
            type: "POST",
            url: "processJSONarray.php",
            data: "pTableData=" + TableData,
            success: function(msg){

            }

         });

    console.log(TableData);

});

