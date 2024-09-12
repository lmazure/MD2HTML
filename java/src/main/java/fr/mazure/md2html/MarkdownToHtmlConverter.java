import org.commonmark.node.Node;
import org.commonmark.parser.Parser;
import org.commonmark.renderer.html.HtmlRenderer;

import java.io.*;
import java.nio.file.*;

public class MarkdownToHtmlConverter {
    public static void main(final String[] args) {
        if (args.length != 2) {
            System.out.println("Usage: java MarkdownToHtmlConverter <input.md> <output.html>");
            return;
        }

        final String inputFile = args[0];
        final String outputFile = args[1];

        try {
            final String markdown = readFile(inputFile);
            final String html = convertToHtml(markdown);
            writeFile(outputFile, html);
            System.out.println("Conversion completed successfully.");
        } catch (final IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }

    private static String readFile(final String filename) throws IOException {
        return new String(Files.readAllBytes(Paths.get(filename)));
    }

    private static void writeFile(final String filename, final String content) throws IOException {
        Files.write(Paths.get(filename), content.getBytes());
    }

    private static String convertToHtml(final String markdown) {
        final Parser parser = Parser.builder().build();
        final Node document = parser.parse(markdown);
        final HtmlRenderer renderer = HtmlRenderer.builder().build();
        return renderer.render(document);
    }
}
