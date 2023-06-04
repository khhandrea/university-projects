import 'package:flutter/material.dart';
import 'package:flutter/gestures.dart';
import 'dart:ui';
import 'package:google_fonts/google_fonts.dart';
import 'utils.dart';

class Scene extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    double baseWidth = 427;
    double fem = MediaQuery.of(context).size.width / baseWidth;
    double ffem = fem * 0.97;
    return Container(
      width: double.infinity,
      child: Container(
        // frame18L6 (587:1745)
        width: double.infinity,
        decoration: BoxDecoration(
          color: Color(0xffffffff),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Container(
              // autogroupfe9cg6i (SRw67uqsJhbvsXBPLAfE9C)
              width: double.infinity,
              height: 275 * fem,
              child: Stack(
                children: [
                  Positioned(
                    // rectangle2901oh8 (586:1689)
                    left: 0 * fem,
                    top: 0 * fem,
                    child: Align(
                      child: SizedBox(
                        width: 427 * fem,
                        height: 228 * fem,
                        child: Container(
                          decoration: BoxDecoration(
                            color: Color(0xff91d168),
                            borderRadius: BorderRadius.only(
                              bottomRight: Radius.circular(2 * fem),
                            ),
                          ),
                        ),
                      ),
                    ),
                  ),
                  Positioned(
                    // rectangle2915i3Q (586:1694)
                    left: 42 * fem,
                    top: 176 * fem,
                    child: Align(
                      child: SizedBox(
                        width: 355 * fem,
                        height: 99 * fem,
                        child: Container(
                          decoration: BoxDecoration(
                            borderRadius: BorderRadius.circular(5 * fem),
                            color: Color(0xffffffff),
                            boxShadow: [
                              BoxShadow(
                                color: Color(0x1c23bcc1),
                                offset: Offset(0 * fem, 3 * fem),
                                blurRadius: 1.5 * fem,
                              ),
                            ],
                          ),
                        ),
                      ),
                    ),
                  ),
                  Positioned(
                    // dailychallengebN6 (586:1695)
                    left: 84 * fem,
                    top: 196 * fem,
                    child: Align(
                      child: SizedBox(
                        width: 95 * fem,
                        height: 18 * fem,
                        child: Text(
                          'Daily Challenge',
                          style: SafeGoogleFont(
                            'Poppins',
                            fontSize: 12 * ffem,
                            fontWeight: FontWeight.w400,
                            height: 1.5 * ffem / fem,
                            color: Color(0xffcacaca),
                          ),
                        ),
                      ),
                    ),
                  ),
                  Positioned(
                    // runorwalkfor30minutesUgn (586:1697)
                    left: 84 * fem,
                    top: 226 * fem,
                    child: Align(
                      child: SizedBox(
                        width: 240 * fem,
                        height: 27 * fem,
                        child: Text(
                          'Run or walk for 30 minutes',
                          style: SafeGoogleFont(
                            'Poppins',
                            fontSize: 18 * ffem,
                            fontWeight: FontWeight.w500,
                            height: 1.5 * ffem / fem,
                            color: Color(0xff88ca5e),
                          ),
                        ),
                      ),
                    ),
                  ),
                  Positioned(
                    // iconawesomestarZy8 (586:1700)
                    left: 69.2823486328 * fem,
                    top: 198.1000061035 * fem,
                    child: Align(
                      child: SizedBox(
                        width: 10.3 * fem,
                        height: 9.86 * fem,
                        child: Image.asset(
                          'assets/icon-awesome-star-wmG.png',
                          width: 10.3 * fem,
                          height: 9.86 * fem,
                        ),
                      ),
                    ),
                  ),
                  Positioned(
                    // ellipse164G6r (586:1701)
                    left: 72 * fem,
                    top: 235 * fem,
                    child: Align(
                      child: SizedBox(
                        width: 5 * fem,
                        height: 5 * fem,
                        child: Container(
                          decoration: BoxDecoration(
                            borderRadius: BorderRadius.circular(2.5 * fem),
                            color: Color(0xff88ca5e),
                          ),
                        ),
                      ),
                    ),
                  ),
                  Positioned(
                    // welcomedavidkimZbk (586:1709)
                    left: 116 * fem,
                    top: 111 * fem,
                    child: Align(
                      child: SizedBox(
                        width: 208 * fem,
                        height: 30 * fem,
                        child: Text(
                          'Welcome, David Kim',
                          style: SafeGoogleFont(
                            'Poppins',
                            fontSize: 20 * ffem,
                            fontWeight: FontWeight.w500,
                            height: 1.5 * ffem / fem,
                            color: Color(0xffffffff),
                          ),
                        ),
                      ),
                    ),
                  ),
                  Positioned(
                    // group1490s6e (586:1712)
                    left: 371 * fem,
                    top: 110 * fem,
                    child: Align(
                      child: SizedBox(
                        width: 16 * fem,
                        height: 29 * fem,
                        child: Image.asset(
                          'assets/group-1490-tHU.png',
                          width: 16 * fem,
                          height: 29 * fem,
                        ),
                      ),
                    ),
                  ),
                  Positioned(
                    // avatarBNE (586:1718)
                    left: 42 * fem,
                    top: 100 * fem,
                    child: Align(
                      child: SizedBox(
                        width: 47 * fem,
                        height: 47 * fem,
                        child: Image.asset(
                          'assets/avatar-8Aa.png',
                          width: 47 * fem,
                          height: 47 * fem,
                        ),
                      ),
                    ),
                  ),
                ],
              ),
            ),
            Container(
              // autogroupz342Vdp (SRw83wTXyu55toahzzz342)
              padding:
                  EdgeInsets.fromLTRB(42 * fem, 18 * fem, 30 * fem, 38 * fem),
              width: double.infinity,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  Container(
                    // autogroup14e21cA (SRw6PKZrobRDdu4F7q14e2)
                    margin: EdgeInsets.fromLTRB(
                        0 * fem, 0 * fem, 0 * fem, 18 * fem),
                    padding: EdgeInsets.fromLTRB(
                        10 * fem, 8 * fem, 17 * fem, 3.5 * fem),
                    width: double.infinity,
                    height: 31 * fem,
                    decoration: BoxDecoration(
                      color: Color(0xffe9ffeb),
                      borderRadius: BorderRadius.circular(5 * fem),
                    ),
                    child: Row(
                      crossAxisAlignment: CrossAxisAlignment.center,
                      children: [
                        Container(
                          // autogroupjamu5c2 (SRw6XZq7u2KoNme3WhJaMU)
                          margin: EdgeInsets.fromLTRB(
                              0 * fem, 0 * fem, 41 * fem, 0 * fem),
                          height: double.infinity,
                          child: Text(
                            'Milestones',
                            style: SafeGoogleFont(
                              'Poppins',
                              fontSize: 12 * ffem,
                              fontWeight: FontWeight.w500,
                              height: 1.5 * ffem / fem,
                              color: Color(0xff156348),
                            ),
                          ),
                        ),
                        Container(
                          // rewardZn6 (586:1705)
                          margin: EdgeInsets.fromLTRB(
                              0 * fem, 0 * fem, 42 * fem, 1.5 * fem),
                          child: Text(
                            'Reward',
                            style: SafeGoogleFont(
                              'Poppins',
                              fontSize: 12 * ffem,
                              fontWeight: FontWeight.w500,
                              height: 1.5 * ffem / fem,
                              color: Color(0xff88ca5e),
                            ),
                          ),
                        ),
                        Container(
                          // social5kS (586:1707)
                          margin: EdgeInsets.fromLTRB(
                              0 * fem, 0 * fem, 42 * fem, 1.5 * fem),
                          child: Text(
                            'Social',
                            style: SafeGoogleFont(
                              'Poppins',
                              fontSize: 12 * ffem,
                              fontWeight: FontWeight.w500,
                              height: 1.5 * ffem / fem,
                              color: Color(0xff88ca5e),
                            ),
                          ),
                        ),
                        Container(
                          // healthaibyg (586:1708)
                          margin: EdgeInsets.fromLTRB(
                              0 * fem, 0 * fem, 0 * fem, 1.5 * fem),
                          child: Text(
                            'Health AI',
                            style: SafeGoogleFont(
                              'Poppins',
                              fontSize: 12 * ffem,
                              fontWeight: FontWeight.w500,
                              height: 1.5 * ffem / fem,
                              color: Color(0xff88ca5e),
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                  Container(
                    // autogroupa4nswGr (SRw6htsF5vcSwxrVzAa4nS)
                    margin: EdgeInsets.fromLTRB(
                        0 * fem, 0 * fem, 0 * fem, 14 * fem),
                    padding: EdgeInsets.fromLTRB(
                        10 * fem, 21 * fem, 10 * fem, 60 * fem),
                    width: double.infinity,
                    decoration: BoxDecoration(
                      color: Color(0xffffffff),
                      borderRadius: BorderRadius.circular(5 * fem),
                      boxShadow: [
                        BoxShadow(
                          color: Color(0x1c23bcc1),
                          offset: Offset(0 * fem, 3 * fem),
                          blurRadius: 1.5 * fem,
                        ),
                      ],
                    ),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.center,
                      children: [
                        Container(
                          // trytoachieveallofyourgoalsyouv (586:1715)
                          margin: EdgeInsets.fromLTRB(
                              0 * fem, 0 * fem, 57 * fem, 23 * fem),
                          child: Text(
                            'Try to achieve all of your goals. You\'ve got this!',
                            style: SafeGoogleFont(
                              'Poppins',
                              fontSize: 12 * ffem,
                              fontWeight: FontWeight.w400,
                              height: 1.5 * ffem / fem,
                              color: Color(0xff000000),
                            ),
                          ),
                        ),
                        Container(
                          // milestoneitemfitnessh9Y (586:1710)
                          margin: EdgeInsets.fromLTRB(
                              0 * fem, 0 * fem, 0 * fem, 25 * fem),
                          padding: EdgeInsets.fromLTRB(
                              18 * fem, 12 * fem, 19 * fem, 16 * fem),
                          width: double.infinity,
                          decoration: BoxDecoration(
                            color: Color(0xffe9ffeb),
                            borderRadius: BorderRadius.circular(5 * fem),
                          ),
                          child: Row(
                            crossAxisAlignment: CrossAxisAlignment.center,
                            children: [
                              Container(
                                // autogroupkuraNmU (SRw71JXuPqC7xFRBvtKUrA)
                                margin: EdgeInsets.fromLTRB(
                                    0 * fem, 10 * fem, 28 * fem, 0 * fem),
                                width: 47 * fem,
                                height: 43 * fem,
                                child: Image.asset(
                                  'assets/auto-group-kura.png',
                                  width: 47 * fem,
                                  height: 43 * fem,
                                ),
                              ),
                              Container(
                                // autogroupjcxnVLJ (SRw76y38h32YJKhNhtJcxN)
                                margin: EdgeInsets.fromLTRB(
                                    0 * fem, 0 * fem, 41 * fem, 3 * fem),
                                child: Column(
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    Container(
                                      // fitnessdBc (I586:1710;231:1592)
                                      margin: EdgeInsets.fromLTRB(
                                          0 * fem, 0 * fem, 0 * fem, 8 * fem),
                                      child: Text(
                                        'Fitness',
                                        style: SafeGoogleFont(
                                          'Poppins',
                                          fontSize: 18 * ffem,
                                          fontWeight: FontWeight.w500,
                                          height: 1.5 * ffem / fem,
                                          color: Color(0xff88ca5e),
                                        ),
                                      ),
                                    ),
                                    Text(
                                      // runa5kinunder30minutesk1L (I586:1710;231:1593)
                                      'Run a 5K in under 30  minutes',
                                      style: SafeGoogleFont(
                                        'Poppins',
                                        fontSize: 12 * ffem,
                                        fontWeight: FontWeight.w400,
                                        height: 1.240000089 * ffem / fem,
                                        color: Color(0xff000000),
                                      ),
                                    ),
                                  ],
                                ),
                              ),
                              Container(
                                // icmorevert24pxsre (I586:1710;231:1595)
                                margin: EdgeInsets.fromLTRB(
                                    0 * fem, 0 * fem, 0 * fem, 27 * fem),
                                width: 4 * fem,
                                height: 16 * fem,
                                child: Image.asset(
                                  'assets/icmorevert24px-iJS.png',
                                  width: 4 * fem,
                                  height: 16 * fem,
                                ),
                              ),
                            ],
                          ),
                        ),
                        Container(
                          // milestoneitemC8E (586:1717)
                          margin: EdgeInsets.fromLTRB(
                              0 * fem, 0 * fem, 0 * fem, 25 * fem),
                          padding: EdgeInsets.fromLTRB(
                              18 * fem, 9 * fem, 19 * fem, 14 * fem),
                          width: double.infinity,
                          height: 81 * fem,
                          decoration: BoxDecoration(
                            color: Color(0xffe9ffeb),
                            borderRadius: BorderRadius.circular(5 * fem),
                          ),
                          child: Row(
                            crossAxisAlignment: CrossAxisAlignment.center,
                            children: [
                              Container(
                                // autogroupfut6gJJ (SRw7esHeNnezYSjqHHFUt6)
                                margin: EdgeInsets.fromLTRB(
                                    0 * fem, 3 * fem, 32 * fem, 0 * fem),
                                width: 43 * fem,
                                height: 49 * fem,
                                child: Image.asset(
                                  'assets/auto-group-fut6.png',
                                  width: 43 * fem,
                                  height: 49 * fem,
                                ),
                              ),
                              Container(
                                // autogroupwqieC1k (SRw7ihWbRtxPqSDqkJwqie)
                                margin: EdgeInsets.fromLTRB(
                                    0 * fem, 0 * fem, 34 * fem, 0 * fem),
                                height: double.infinity,
                                child: Column(
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    Container(
                                      // fitnessXZp (I586:1717;281:1624)
                                      margin: EdgeInsets.fromLTRB(
                                          0 * fem, 0 * fem, 0 * fem, 1 * fem),
                                      child: Text(
                                        'Dietary',
                                        style: SafeGoogleFont(
                                          'Poppins',
                                          fontSize: 18 * ffem,
                                          fontWeight: FontWeight.w500,
                                          height: 1.5 * ffem / fem,
                                          color: Color(0xff88ca5e),
                                        ),
                                      ),
                                    ),
                                    Container(
                                      // drink8glassesofwatereverydayfo (I586:1717;281:1632)
                                      constraints: BoxConstraints(
                                        maxWidth: 185 * fem,
                                      ),
                                      child: Text(
                                        'Drink 8 glasses of water every-\nday for a week',
                                        style: SafeGoogleFont(
                                          'Poppins',
                                          fontSize: 12 * ffem,
                                          fontWeight: FontWeight.w400,
                                          height: 1.240000089 * ffem / fem,
                                          color: Color(0xff000000),
                                        ),
                                      ),
                                    ),
                                  ],
                                ),
                              ),
                              Container(
                                // icmorevert24pxMok (I586:1717;281:1626)
                                margin: EdgeInsets.fromLTRB(
                                    0 * fem, 0 * fem, 0 * fem, 26 * fem),
                                width: 4 * fem,
                                height: 16 * fem,
                                child: Image.asset(
                                  'assets/icmorevert24px-Wcv.png',
                                  width: 4 * fem,
                                  height: 16 * fem,
                                ),
                              ),
                            ],
                          ),
                        ),
                        Container(
                          // component203UtN (586:1711)
                          padding: EdgeInsets.fromLTRB(
                              18 * fem, 12 * fem, 19 * fem, 16 * fem),
                          width: double.infinity,
                          decoration: BoxDecoration(
                            color: Color(0xffe9ffeb),
                            borderRadius: BorderRadius.circular(5 * fem),
                          ),
                          child: Row(
                            crossAxisAlignment: CrossAxisAlignment.center,
                            children: [
                              Container(
                                // autogrouprti6bCJ (SRw7Mxc9mdmR6dr6sprTi6)
                                margin: EdgeInsets.fromLTRB(
                                    0 * fem, 5 * fem, 32 * fem, 0 * fem),
                                width: 43 * fem,
                                height: 48 * fem,
                                child: Image.asset(
                                  'assets/auto-group-rti6.png',
                                  width: 43 * fem,
                                  height: 48 * fem,
                                ),
                              ),
                              Container(
                                // autogroupypyeuyg (SRw7Rnq6pk4pPdL7LrYpYe)
                                margin: EdgeInsets.fromLTRB(
                                    0 * fem, 0 * fem, 93 * fem, 3 * fem),
                                child: Column(
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    Container(
                                      // personalgoalTEW (I586:1711;231:1592)
                                      margin: EdgeInsets.fromLTRB(
                                          0 * fem, 0 * fem, 0 * fem, 8 * fem),
                                      child: Text(
                                        'Personal Goal',
                                        style: SafeGoogleFont(
                                          'Poppins',
                                          fontSize: 18 * ffem,
                                          fontWeight: FontWeight.w500,
                                          height: 1.5 * ffem / fem,
                                          color: Color(0xff88ca5e),
                                        ),
                                      ),
                                    ),
                                    Text(
                                      // hitnormalbmia4E (I586:1711;231:1593)
                                      'Hit normal BMI',
                                      style: SafeGoogleFont(
                                        'Poppins',
                                        fontSize: 12 * ffem,
                                        fontWeight: FontWeight.w400,
                                        height: 1.240000089 * ffem / fem,
                                        color: Color(0xff000000),
                                      ),
                                    ),
                                  ],
                                ),
                              ),
                              Container(
                                // icmorevert24px7Zx (I586:1711;231:1595)
                                margin: EdgeInsets.fromLTRB(
                                    0 * fem, 0 * fem, 0 * fem, 27 * fem),
                                width: 4 * fem,
                                height: 16 * fem,
                                child: Image.asset(
                                  'assets/icmorevert24px-Jjg.png',
                                  width: 4 * fem,
                                  height: 16 * fem,
                                ),
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),
                  ),
                  Container(
                    // autogroupjy7ge46 (SRw7tSjMdawGFjpWkyJY7G)
                    width: double.infinity,
                    height: 68 * fem,
                    child: Stack(
                      children: [
                        Positioned(
                          // rectangle3032PGa (586:1699)
                          left: 0 * fem,
                          top: 0 * fem,
                          child: Align(
                            child: SizedBox(
                              width: 355 * fem,
                              height: 68 * fem,
                              child: Container(
                                decoration: BoxDecoration(
                                  borderRadius: BorderRadius.circular(34 * fem),
                                  color: Color(0xffffffff),
                                  boxShadow: [
                                    BoxShadow(
                                      color: Color(0x1c23bcc1),
                                      offset: Offset(0 * fem, 3 * fem),
                                      blurRadius: 1.5 * fem,
                                    ),
                                  ],
                                ),
                              ),
                            ),
                          ),
                        ),
                        Positioned(
                          // taptoconnectapplewatch59Q (586:1702)
                          left: 96 * fem,
                          top: 27 * fem,
                          child: Align(
                            child: SizedBox(
                              width: 171 * fem,
                              height: 18 * fem,
                              child: Text(
                                'Tap to connect Apple Watch',
                                style: SafeGoogleFont(
                                  'Poppins',
                                  fontSize: 12 * ffem,
                                  fontWeight: FontWeight.w400,
                                  height: 1.5 * ffem / fem,
                                  color: Color(0xffcacaca),
                                ),
                              ),
                            ),
                          ),
                        ),
                        Positioned(
                          // image221ZqG (586:1716)
                          left: 65 * fem,
                          top: 19 * fem,
                          child: Align(
                            child: SizedBox(
                              width: 21 * fem,
                              height: 31 * fem,
                              child: Image.asset(
                                'assets/image-221-Hyx.png',
                                fit: BoxFit.cover,
                              ),
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
