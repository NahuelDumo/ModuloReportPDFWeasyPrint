import logging
from odoo import models, api
from weasyprint import HTML
import base64

_logger = logging.getLogger(__name__)

class IrActionsReport(models.Model):
    _inherit = "ir.actions.report"

    def _render_qweb_pdf(self, res_ids=None, data=None):
        """Sobrescribir el método para usar WeasyPrint."""
        _logger.info("⚡ Usando WeasyPrint para generar el PDF ⚡")

        # Renderizar el contenido HTML
        html_content, _ = self._render_qweb_html(res_ids, data=data)

        _logger.info("✅ HTML para PDF renderizado correctamente.")

        # Usar WeasyPrint para convertir HTML a PDF
        try:
            pdf = HTML(string=html_content).write_pdf()
            _logger.info("✅ PDF generado con éxito usando WeasyPrint.")
        except Exception as e:
            _logger.error(f"❌ Error al generar PDF con WeasyPrint: {e}")
            raise

        return pdf, "pdf"

    def _render_qweb_html(self, res_ids=None, data=None):
        """Método original para renderizar HTML (puedes sobrescribir si necesitas ajustes)."""
        _logger.info("🎨 Renderizando HTML antes de la conversión a PDF.")
        return super()._render_qweb_html(res_ids=res_ids, data=data)
