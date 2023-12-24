import 'package:flutter/material.dart';

void main(){
  runApp(ColumnWidgetExample());
}

class ColumnWidgetExample extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    return MaterialApp(
      home:Scaffold(
        body:SizedBox(
          height: double.infinity,
          child: Stack(
            children:[
              Container(
                height:300.0,
                width:300.0,
                color:Colors.red,
              ),
              Container(
                height:250.0,
                width:250.0,
                color:Colors.yellow,
              ),
              Container(
                height:200.0,
                width:200.0,
                color:Colors.blue,
              ),
            ],
          ),
        ),
      ),
    );
  }
}