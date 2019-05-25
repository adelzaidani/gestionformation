$('#save_attendance').click(function(){
    var TableData;
    TableData = saveTable()
    TableData = $.toJSON(TableData);
    date_selected=new Date($('#date_attendance').val());
    date_begin=new Date($('#date_of_begin').val());
    date_finish=new Date($('#date_of_finish').val());


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
                    alert(data.message);
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
        url:"/teacher/list_attendance_date_change",
        data:{'date_selected':date_string,
              'session':session
              },
        dataType:'Json',
        success:function(data){

           $.each(data, function(){

              $("#tr-" + this.id_student + " td.id_student").html(this.id_student);
              $("#tr-" + this.id_student + " td.last_name").html(this.last_name);
              $("#tr-" + this.id_student + " td.first_name").html(this.first_name);
              $("#tr-" + this.id_student + " td.birth_date").html(this.birth_date);
              if (this.attendance == 1){
                $("#check_attendance-" +this.id_student).attr('checked', true);

              }
              else{
                 $("#check_attendance-" +this.id_student).attr('checked', false);
              }






            });

        }

    });

});


