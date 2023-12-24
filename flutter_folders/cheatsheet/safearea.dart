import 'package:flutter/material.dart';

void main() {
  runApp(
      MyApp()

  );
}

class MyApp extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    return MaterialApp(
      home: Scaffold(
        body: Center(
          child:SafeArea(
            top:true,
            bottom:true,
            left:true,
            right:true,
            child:Container(
              color:Colors.red,
              height:3000.0,
              width:3000.0,
            ),
          ),
        ),
      ),
    );
  }
}
