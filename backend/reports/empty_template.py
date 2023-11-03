text = """<!DOCTYPE document SYSTEM "rml.dtd">
<document filename="my_story.pdf">
 <template>
     <!-- Данная секция содержит элементы документа с фиксированной позицией -->
     <pageTemplate id="main">
        <frame id="first" x1="100" y1="400" width="300" height="400"/>
     </pageTemplate>
 </template>
 <stylesheet>
     <!-- Данная секция содержит информацию о стилях -->
     <paraStyle name="header" fontSize="16" fontName="Arial" leading="16"/>
 </stylesheet>
 <story>
    <!-- Этот раздел содержит плавающие элементы документа. Эти элементы будут заполнять фреймы, определенные в -->
    <!-- разделе <template> выше -->

    <para style="header">
        <b>Мой первый отчет в RML</b>
    </para>
    <para></para>
 </story>
</document>"""