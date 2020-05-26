import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import org.jsoup.nodes.TextNode;
import org.jsoup.nodes.Node;
import org.jsoup.Connection;
import java.io.IOException;

class Lyrics {

  public static String getUrl(String title, String artist) {
    String[] title_words = title.replaceAll("[^a-zA-Z0-9]"," ").toLowerCase().split("\\s+");
    String[] artist_words = artist.replaceAll("[^a-zA-Z0-9]"," ").toLowerCase().split("\\s+");
    title="";
    artist="";
    for (String word : title_words) {
      if (!word.equals(""))
        title+= word +"-";
    }
    for (String word : artist_words){
      if (!word.equals(""))
        artist+= word +"-";
    }
    String url = "https://www.genius.com/"+artist+title+"lyrics";
    return url;
  }

  public static String getLyrics(String url) {
    String lyrics = "";
    try {
      Document doc = Jsoup.connect(url).get();
      Element song = doc.select("div.lyrics").get(0);
      lyrics = song.wholeText();
      System.out.println(lyrics);
    }
    catch (IOException e) {
      System.out.println("Lyrics not found");
      return null;
    }
    return lyrics;
  }
}
