public class Assignment_08 {
    public static void main(String[] args) {
        System.out.println("202111278 김환희");
        MyTv tv1 = new MyTv();
        System.out.println("[tv1 정보]");
        System.out.println("전원: "+(tv1.isPowerOn ? "on" : "off")+" / 채널: "+tv1.channel+" / 볼륨: "+tv1.volume+"\n");
        MyTv tv2 = new MyTv(true);
        System.out.println("[tv2 정보]");
        System.out.println("전원: "+(tv2.isPowerOn ? "on" : "off")+" / 채널: "+tv2.channel+" / 볼륨: "+tv2.volume+"\n");
        MyTv tv3 = new MyTv(true, 26);
        System.out.println("[tv3 정보]");
        System.out.println("전원: "+(tv3.isPowerOn ? "on" : "off")+" / 채널: "+tv3.channel+" / 볼륨: "+tv3.volume+"\n");
        MyTv tv4 = new MyTv(true, 26, 3); System.out.println("[tv4 정보]");
        tv4.turnOnOff(); tv4.channelDown(); tv4.volumeDown();
        System.out.println("전원: "+(tv4.isPowerOn ? "on" : "off")+" / 채널: "+tv4.channel+" / 볼륨: "+tv4.volume+"\n");
        MyTv tv5 = new MyTv(true, 99, 9);
        System.out.println("[tv5 정보]");
        tv5.channelUp(); tv5.channelUp(); tv5.channelUp(); tv5.volumeUp(); tv5.volumeUp(); tv5.volumeUp();
        System.out.println("전원: "+(tv5.isPowerOn ? "on" : "off")+" / 채널: "+tv5.channel+" / 볼륨: "+tv5.volume+"\n"); 
    }
}

class MyTv {
    boolean isPowerOn;
    int channel;
    int volume;

    MyTv() {
        this(false, 1, 5);
    }

    MyTv(boolean isPowerOn) {
        this(isPowerOn, 1, 5);
    }

    MyTv(boolean isPowerOn, int channel) {
        this(isPowerOn, channel, 5);
    }

    MyTv(boolean isPowerOn, int channel, int volume) {
        this.isPowerOn = isPowerOn;
        this.channel = channel;
        this.volume = volume;
    }

    void turnOnOff() { isPowerOn = !isPowerOn; }

    void channelUp() {
        if(channel < 100) channel += 1; 
    }

    void channelDown() { 
        if(channel > 1) channel -= 1;
    }

    void volumeUp() {
        if(volume < 10) volume += 1;
    }

    void volumeDown() {
        if(volume > 0) volume -= 1;
    }
 }