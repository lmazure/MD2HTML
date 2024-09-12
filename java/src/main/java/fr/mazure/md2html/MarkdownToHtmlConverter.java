import org.commonmark.node.*;
import org.commonmark.parser.Parser;
import org.commonmark.renderer.html.HtmlRenderer;

import java.io.*;
import java.nio.file.*;

public class MarkdownToHtmlConverter {
    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Usage: java MarkdownToHtmlConverter <input.md> <output.html>");
            return;
        }

        String inputFile = args[0];
        String outputFile = args[1];

        try {
            String markdown = readFile(inputFile);
            String html = convertToHtml(markdown);
            writeFile(outputFile, html);
            System.out.println("Conversion completed successfully.");
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }

    private static String readFile(String filename) throws IOException {
        return new String(Files.readAllBytes(Paths.get(filename)));
    }

    private static void writeFile(String filename, String content) throws IOException {
        Files.write(Paths.get(filename), content.getBytes());
    }

    private static String convertToHtml(String markdown) {
        Parser parser = Parser.builder().build();
        Node document = parser.parse(markdown);
        HtmlRenderer renderer = HtmlRenderer.builder().build();
        return renderer.render(document);
    }
}
