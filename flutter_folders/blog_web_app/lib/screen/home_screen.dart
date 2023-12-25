import 'package:flutter/material.dart';

import 'package:webview_flutter/webview_flutter.dart';

class HomeScreen extends StatelessWidget{
  WebViewController? controller;
  HomeScreen({Key? key}) : super(key: key);

  Widget build(BuildContext context){
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.orange,
        title: Text('My Love'),
        centerTitle: true,

        actions:[
          IconButton(
            onPressed: () {
              if(controller != null){
                controller!.loadUrl('https://ai.dongguk.edu/professor/list?professor_haggwa_type=PROFH_151&professor_type=PROF_006');
              }
            },
            icon: Icon(
              Icons.home,
            ),
          ),
        ],
      ),
      body:WebView(
        onWebViewCreated: (WebViewController controller){
          this.controller = controller;
        },

        initialUrl: 'https://dwkim606.github.io',
        javascriptMode: JavascriptMode.unrestricted,
      ),
    );
  }
}