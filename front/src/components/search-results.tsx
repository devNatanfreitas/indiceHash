import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { CheckCircle, XCircle, Clock, Database, FileText } from "lucide-react"

interface SearchResultsProps {
  result: {
    tempo_busca: string
    encontrado: boolean
    resultado: any
    pagina_id?: number
    custo: number
  }
  type: "hash" | "scan"
  searchKey: string
}

export function SearchResults({ result, type, searchKey }: SearchResultsProps) {
  const isHash = type === "hash"

  return (
    <Card className={`border-2 ${result.encontrado ? "border-green-200 bg-green-50" : "border-red-200 bg-red-50"}`}>
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          {result.encontrado ? (
            <CheckCircle className="w-5 h-5 text-green-600" />
          ) : (
            <XCircle className="w-5 h-5 text-red-600" />
          )}
          Resultado da Busca {isHash ? "por Índice Hash" : "por Table Scan"}
        </CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div className="text-center p-3 bg-white rounded-lg border">
            <Clock className="w-6 h-6 mx-auto mb-2 text-blue-600" />
            <div className="text-sm text-gray-600">Tempo</div>
            <div className="font-semibold">{result.tempo_busca}</div>
          </div>

          <div className="text-center p-3 bg-white rounded-lg border">
            <Database className="w-6 h-6 mx-auto mb-2 text-purple-600" />
            <div className="text-sm text-gray-600">Custo (I/O)</div>
            <div className="font-semibold">{result.custo} acessos</div>
          </div>

          {isHash && result.pagina_id !== undefined && (
            <div className="text-center p-3 bg-white rounded-lg border">
              <FileText className="w-6 h-6 mx-auto mb-2 text-green-600" />
              <div className="text-sm text-gray-600">Página</div>
              <div className="font-semibold">#{result.pagina_id}</div>
            </div>
          )}

          <div className="text-center p-3 bg-white rounded-lg border">
            <div className="text-sm text-gray-600">Status</div>
            <Badge variant={result.encontrado ? "default" : "destructive"} className="mt-1">
              {result.encontrado ? "Encontrado" : "Não encontrado"}
            </Badge>
          </div>
        </div>

        {result.encontrado && result.resultado && (
          <div className="p-4 bg-white rounded-lg border">
            <div className="text-sm text-gray-600 mb-2">Registro encontrado:</div>
            <div className="font-mono text-sm bg-gray-50 p-3 rounded border">
              Chave: "{searchKey}"{result.resultado.dados && <div>Dados: {JSON.stringify(result.resultado.dados)}</div>}
            </div>
          </div>
        )}
      </CardContent>
    </Card>
  )
}
