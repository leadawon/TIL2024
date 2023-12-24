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
          child:GestureDetector(
            onTap:(){
              print('on tap');
            },

            onDoubleTap: (){
              print('on double tap');
            },

            onLongPress: (){
              print('on long press');
            },

            child: ElevatedButton(
              onPressed: (){},
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.red,
              ),
              child: Text('elevated button'),
            ),
          ),
        ),
      ),
    );
  }
}
