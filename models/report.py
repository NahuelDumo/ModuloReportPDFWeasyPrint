from odoo import models, api
from weasyprint import HTML
import base64

class IrActionsReport(models.Model):
    _inherit = "ir.actions.report"

    def _render_qweb_pdf(self, res_ids=None, data=None):
        """Sobrescribir el método para usar WeasyPrint."""
        # Renderizar el contenido HTML
        html_content, _ = self._render_qweb_html(res_ids, data=data)

        # Usar WeasyPrint para convertir HTML a PDF
        pdf = HTML(string=html_content).write_pdf()

        return pdf, "pdf"

    def _render_qweb_html(self, res_ids=None, data=None):
        """Método original para renderizar HTML (puedes sobrescribir si necesitas ajustes)."""
        return super()._render_qweb_html(res_ids=res_ids, data=data)
