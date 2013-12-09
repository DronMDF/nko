<xsl:stylesheet version = '1.0'
     xmlns:xsl='http://www.w3.org/1999/XSL/Transform'>
<xsl:output method="text"/>

<xsl:template match="/">
	<xsl:for-each select='//table[@id="pdg"]/tbody/tr[position() > 2]'>
		<xsl:value-of select="@id"/>
		<xsl:text>&#10;</xsl:text>
		<xsl:value-of select="td[2]"/>
		<xsl:text>&#10;</xsl:text>
		<xsl:value-of select="td[4]"/>
		<xsl:text>&#10;</xsl:text>
		<xsl:value-of select="td[6]"/>
		<xsl:text>&#10;</xsl:text>
		<xsl:value-of select="td[8]"/>
		<xsl:text>&#10;</xsl:text>
		<xsl:value-of select="td[10]"/>
		<xsl:text>&#10;</xsl:text>
		<xsl:value-of select="td[12]"/>
		<xsl:text>&#10;</xsl:text>
		<xsl:text>--- separator ---&#10;</xsl:text>
	</xsl:for-each>
</xsl:template>
</xsl:stylesheet>

