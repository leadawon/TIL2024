import 'package:flutter/material.dart';

class EmoticonSticker extends StatefulWidget{
  final VoidCallback onTransform;
  final String imgPath;
  final bool isSelected;

  const EmoticonSticker({
    required this.onTransform,
    required this.imgPath,
    required this.isSelected,
    Key? key,
}): super(key: key);


  @override
  State<EmoticonSticker> createState() => _EmotionStickerState();
}

class _EmotionStickerState extends State<EmoticonSticker> {
  @override
  Widget build(BuildContext context){
    return Transform(
      transform: Matrix4.identity()
          ..translate(hTransform, vTransform)
          ..scale(scale,scale),
      child:     Container(
        decoration: widget.isSelected
            ? BoxDecoration(
          borderRadius: BorderRadius.circular(4.0),
          border: Border.all(
            color: Colors.blue,
            width: 1.0,
          ),
        )
            : BoxDecoration(
          border: Border.all(
            width: 1.0,
            color: Colors.transparent,
          ),
        ),
        child: GestureDetector(
          onTap: () {
            widget.onTransform();
            setState((){
              scale = details.scale * actualScale;
              vTransform += details.focalPointDelta.dy;
              hTransform += details.focalPointDelta.dx;
            });
          },
          onScaleUpdate: (ScaleUpdateDetails details){
            actualScale = scale;
          },
          onScaleEnd: (ScaleEndDetails details) {},
          child: Image.asset(
            widget.imgPath,
          ),
        ),
      ),
    )


  }
}