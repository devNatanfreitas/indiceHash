import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"

interface TableScanVisualizationProps {
  records: string[]
  isScanning: boolean
}

export function TableScanVisualization({ records, isScanning }: TableScanVisualizationProps) {
  return (
    <Card>
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          <div className={`w-3 h-3 rounded-full ${isScanning ? "bg-yellow-500 animate-pulse" : "bg-gray-400"}`}></div>
          Progresso do Table Scan
        </CardTitle>
      </CardHeader>
      <CardContent>
        <div className="space-y-3">
          {records.length === 0 && !isScanning && (
            <div className="text-gray-500 text-center py-8">
              Nenhum scan executado ainda. Digite uma palavra e clique em "Iniciar Table Scan".
            </div>
          )}

          {records.map((record, index) => (
            <div key={index} className="flex items-center gap-3 p-3 bg-gray-50 rounded-lg">
              <Badge variant="outline" className="min-w-fit">
                {index + 1}
              </Badge>
              <span className="font-mono text-sm">{record}</span>
            </div>
          ))}

          {isScanning && (
            <div className="flex items-center gap-3 p-3 bg-yellow-50 rounded-lg border border-yellow-200">
              <div className="w-4 h-4 border-2 border-yellow-500 border-t-transparent rounded-full animate-spin"></div>
              <span className="text-yellow-800">Escaneando páginas...</span>
            </div>
          )}
        </div>
      </CardContent>
    </Card>
  )
}
