import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'dart:math';
import 'package:intl/intl.dart';
import 'view_profile.dart';

class Edit_profile extends StatelessWidget {
  List<String> userInputList = List<String>.filled(5, '');
  static const routeName = '/profile';
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
                        "Please enter your details",
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
                    _personalDetailInfo(0,  "assets/Icon awesome.png"),
                    _personalDetailInfo(1,  "assets/cake.png"),
                    _personalDetailInfo(2,  "assets/phone.png"),
                    _personalDetailInfo(3,  "assets/instagram.png"),
                    _personalDetailInfo(4,  "assets/mail.png"),
                    _personalDataInfoButton(context, userInputList),
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

  Widget _personalDetailInfo(int index, String imagePath) {
    TextEditingController controller = TextEditingController();
    String shadowText = '';
    switch (index) {
      case 0:
        shadowText = 'Enter Your Name';
        break;
      case 1:
        shadowText = 'Enter your birthdate';
        break;
      case 2:
        shadowText = 'Enter your phone number';
        break;
      case 3:
        shadowText = 'Enter your Instagram username';
        break;
      case 4:
        shadowText = 'Enter your email address';
        break;
    }

    return Container(
      margin: EdgeInsets.only(bottom: 10),
      child: Row(
        children: [
          Container(
            width: 24,
            height: 24,
            child: Image.asset(imagePath),
          ),
          SizedBox(width: 8),
          Expanded(
            child: TextFormField(
              controller: controller,
              onChanged: (value) {
                userInputList[index] = value;
              },
              decoration: InputDecoration(
                contentPadding:
                EdgeInsets.symmetric(vertical: 12, horizontal: 16),
                enabledBorder: const OutlineInputBorder(
                  borderSide: BorderSide(
                    width: 1,
                    color: Colors.lightGreen,
                  ),
                  borderRadius: BorderRadius.all(Radius.circular(5)),
                ),
                focusedBorder: const OutlineInputBorder(
                  borderSide: BorderSide(
                    width: 1,
                    color: Colors.green,
                  ),
                  borderRadius: BorderRadius.all(Radius.circular(10)),
                ),
                hintText: shadowText,
                hintStyle: TextStyle(
                  color: Colors.grey,
                  fontStyle: FontStyle.italic,
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }

  ElevatedButton _personalDataInfoButton(BuildContext context, List<String> userInputList) {
    return ElevatedButton(
      style: ButtonStyle(
        foregroundColor: MaterialStatePropertyAll(Colors.white),
        backgroundColor: MaterialStatePropertyAll(Colors.green.shade300),
        fixedSize: MaterialStatePropertyAll(Size(160, 50)),
        elevation: MaterialStatePropertyAll(3),
      ),
      onPressed: () {
        // Navigate to another page when the button is pressed
        Navigator.push(
          context,
          MaterialPageRoute(
              builder: (context) => View_ProfilePage(userInputList : userInputList)
          ),
        );
      },
      child: const Text(
        "SAVE",
        style: TextStyle(
          fontSize: 17,
          fontWeight: FontWeight.bold,
        ),
      ),
    );
  }
}