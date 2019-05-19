$.ajax({
            type: "POST",
            url: "/teacher/save_attendance/",
            data: "pTableData=" + TableData,
            success: function(data, status){
                console.log(data["HTTPRESPONSE"]);

             },
             error:function(result,status,error){

             },
             complete:function(result,status){

             }


         });