import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'dart:math';
import 'package:intl/intl.dart';

class View_ProfilePage extends StatelessWidget {
  final List<String> userInputList;

  View_ProfilePage({required this.userInputList});
  static const routeName = '/view_profile';
  @override
  Widget build(BuildContext context) {

    Widget getInfoSection = Card(
      margin: const EdgeInsets.fromLTRB(15, 0, 15, 0),
      elevation: 0,
      child: Column(
        // mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: [
          Expanded(
              flex: 1,
              child: Column(
                children: [
                  Expanded(
                    flex: 5,
                    child: CircleAvatar(
                      backgroundImage: AssetImage('assets/avatar1.png'),
                      radius: 60,
                    ),
                  ),
                  Expanded(
                      flex: 2,
                      child: Text(
                        "Welcome To Profile Page",
                        style: TextStyle(
                          color: Colors.green.shade500,
                          fontSize: 20,
                        ),
                      )
                  )
                ],
              )
          ),
          Expanded(
            flex: 2,
            child: SingleChildScrollView(
                child : Column(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    _personalDetailInfo(userInputList[0],"assets/Icon awesome.png"),
                    _personalDetailInfo(userInputList[1], "assets/cake.png"),
                    _personalDetailInfo(userInputList[2], "assets/phone.png"),
                    _personalDetailInfo(userInputList[3], "assets/instagram.png"),
                    _personalDetailInfo(userInputList[4], "assets/mail.png"),
                    _personalDataInfoButton(),
                  ],
                )
            ),
          )
        ],
      ),
    );

    return AnnotatedRegion<SystemUiOverlayStyle>(
      value: SystemUiOverlayStyle.dark,
      child : Stack (
        children : [
          Container(
              decoration: BoxDecoration(
                gradient: LinearGradient(
                    begin: Alignment.topLeft,
                    end: Alignment.bottomRight,
                    colors: [ Colors.white, Colors.green.shade200 ]
                ),
              ),
              child: Column(
                children: [
                  Expanded(
                      flex: 2,
                      child: Container(
                          decoration: const BoxDecoration(
                              image: DecorationImage(
                                  image: AssetImage('assets/robot-lookDown.png'),
                                  fit: BoxFit.cover
                              )
                          )
                      )
                  ),
                  Expanded(
                    flex: 10,
                    child: Container(
                      margin: const EdgeInsets.fromLTRB(20, 0, 20, 50),
                      height: double.infinity,
                      width: double.infinity,
                      decoration: const BoxDecoration(
                          color: Colors.white,
                          borderRadius: BorderRadius.all(Radius.circular(8)),
                          boxShadow: [
                            BoxShadow(
                              color: Colors.grey,
                              spreadRadius: 1,
                              blurRadius: 3,
                              offset: Offset(0, 3),
                            )
                          ]
                      ),
                      child: getInfoSection,
                    ),
                  )
                ],
              )
          ),
          Positioned(
            top: 48,
            right: 8,
            child: GestureDetector(
              onTap: () {
                Navigator.pop(context);
              },
              child: Image.asset(
                'assets/back_btn.png',
                width: 60,
                height: 60,
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _personalDetailInfo(String value, String imagePath) {
    return Container(
      margin: EdgeInsets.only(bottom: 10), // Add margin of 8 pixels at the bottom
      child: Row(
        children: [
          Container(
            width: 24,
            height: 24,
            child : Image.asset(imagePath), // Image widget
          ),
          SizedBox(width: 8),
          Expanded(
            child : TextFormField(// Add a space between the image and the TextFormField
              readOnly: true,
              initialValue: value,
              decoration: InputDecoration(
                contentPadding: EdgeInsets.symmetric(vertical: 12, horizontal: 16),
                enabledBorder: const OutlineInputBorder(
                    borderSide: BorderSide(
                      width: 1, color: Colors.lightGreen,
                    ),
                    borderRadius: BorderRadius.all(Radius.circular(5))
                ),
                focusedBorder: const OutlineInputBorder(
                    borderSide: BorderSide(
                      width: 1, color: Colors.green,
                    ),
                    borderRadius: BorderRadius.all(Radius.circular(10))
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }

  ElevatedButton _personalDataInfoButton() {
    return ElevatedButton(
      style: ButtonStyle(
          foregroundColor: const MaterialStatePropertyAll(Colors.white),
          backgroundColor: MaterialStatePropertyAll(Colors.green.shade300),
          fixedSize: const MaterialStatePropertyAll(Size(160, 50)),
          elevation: const MaterialStatePropertyAll(3)
      ),
      onPressed: null, // TODO have to be implemented 'onPressed'
      child: const Text(
        "SAVE",
        style: TextStyle(
            fontSize: 17,
            fontWeight: FontWeight.bold
        ),
      ),
    );
  }
}