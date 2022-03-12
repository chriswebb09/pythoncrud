function search(term) {
    if (!term || term.length == 0) {
        return;
    } else {
        window.location.assign("/search/" + term);
    }
   
 }

 $(document).ready(function() {
   $("#search_button").click(function() {
       let text = $("#search_input").val();
       if (text.trim().length == 0) {
           return;
       }
       search(text);
       $("#search_input").val("");
   })
 });