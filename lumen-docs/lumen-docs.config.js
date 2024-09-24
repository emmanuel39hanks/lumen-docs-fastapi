
module.exports = {
  outputDir: 'docs/',
  gitbookDeploy: {
    enabled: false,
    gitbookApiKey: process.env.LUMEN_DOCS_GITBOOK_API_KEY,
    gitbookSpaceId: process.env.LUMEN_DOCS_GITBOOK_SPACE_ID,
  },
  openai: {
    apiKey: process.env.LUMEN_DOCS_OPENAI_API_KEY,
    model: 'gpt-4',
    tone: 'formal',
    temperature: 0.2,
  },
  versions: {
    enabled: true,
    keepVersions: 5,
  },
};
