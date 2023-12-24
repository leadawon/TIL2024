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
          child: Column(
            children:[
              Expanded(
                flex:3,
                child:Container(
                  color:Colors.blue,
                ),
              ),
              Expanded(
                child:Container(
                  color:Colors.red,
                ),
              )
            ],
          ),
        ),
      ),
    );
  }
}